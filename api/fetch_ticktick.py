#!/usr/bin/env python3
"""
TickTick Task Fetcher - Robust version with retries
"""

import requests
import json
from datetime import datetime, timedelta, timezone
import os
import time

def get_api_key():
    """Load API key from ~/.ticktick_env"""
    env_file = os.path.expanduser("~/.ticktick_env")
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"~/.ticktick_env ikke fundet")
    with open(env_file, 'r') as f:
        for line in f:
            if line.startswith('TICKTICK_API_KEY='):
                key = line.split('=', 1)[1].strip()
                if key:
                    return key
    raise ValueError("TICKTICK_API_KEY ikke fundet i ~/.ticktick_env")

BASE_URL = "https://api.ticktick.com/open/v1"

def api_get(url, headers, max_retries=3):
    for attempt in range(max_retries):
        try:
            r = requests.get(url, headers=headers, timeout=15, verify=True)
            return r
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            pass
        except Exception:
            pass
        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)
    return None

def fetch_ticktick_with_retry(api_key, max_retries=3):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Step 1: fetch all projects
    r = api_get(f"{BASE_URL}/project", headers, max_retries)
    if r is None:
        return {"error": "Could not connect to TickTick API"}, None
    if r.status_code == 401:
        return {"error": f"Unauthorized (401) — check API key: {r.text[:200]}"}, None
    if r.status_code != 200:
        return {"error": f"Unexpected status {r.status_code} fetching projects: {r.text[:200]}"}, None

    projects = r.json()
    all_tasks = []
    for project in projects:
        pid = project.get("id")
        if not pid:
            continue
        r2 = api_get(f"{BASE_URL}/project/{pid}/data", headers, max_retries)
        if r2 and r2.status_code == 200:
            all_tasks.extend(r2.json().get("tasks", []))

    return {"tasks": all_tasks}, BASE_URL

import re

def normalize_date(raw):
    raw = raw.replace('Z', '+00:00')
    raw = re.sub(r'([+-])(\d{2})(\d{2})$', r'\1\2:\3', raw)
    return datetime.fromisoformat(raw)

def parse_tasks(data):
    """Parse TickTick response — all tasks, grouped by due date or 'no_date'"""
    if "error" in data:
        return {}

    tasks = data.get('tasks', [])
    result = {}

    for task in tasks:
        if task.get('status') == 2:  # skip completed
            continue

        due_raw = task.get('dueDate') or task.get('startDate')
        if due_raw:
            try:
                due_date = normalize_date(due_raw)
                date_key = due_date.strftime("%Y-%m-%d")
            except Exception:
                date_key = "unknown_date"
        else:
            date_key = "no_date"

        result.setdefault(date_key, []).append({
            "title": task.get('title', 'Untitled'),
            "priority": task.get('priority', 0),
            "completed": task.get('status') == 2,
            "description": task.get('content', ''),
            "project": task.get('projectId', ''),
        })

    for key in result:
        result[key].sort(key=lambda x: x['priority'], reverse=True)

    return result

if __name__ == "__main__":
    try:
        api_key = get_api_key()
    except (FileNotFoundError, ValueError) as e:
        print(f"TICKTICK_ERROR: {e}")
        exit(1)
    data, endpoint = fetch_ticktick_with_retry(api_key)

    if "error" in data and endpoint is None:
        print("TICKTICK_ERROR: " + data.get("error", "Unknown error"))
    else:
        tasks = parse_tasks(data)
        print("TICKTICK_SUCCESS")
        print(json.dumps(tasks, indent=2, default=str))
