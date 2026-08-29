#!/usr/bin/env bash
# Merge the dotfiles-managed cron jobs into the existing crontab.
#
# The old approach was `crontab ./misc/cronjobs`, which REPLACES the entire
# crontab — silently destroying any job not in that file. This instead strips
# only the previously-managed block and re-appends the current one, leaving
# every other job untouched. Safe to run repeatedly.
set -euo pipefail
BASEDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANAGED="$BASEDIR/cronjobs"

[ -f "$MANAGED" ] || { echo "no $MANAGED, skipping cron setup"; exit 0; }

existing="$(crontab -l 2>/dev/null || true)"
preserved="$(printf '%s\n' "$existing" | sed '/# BEGIN dotfiles-managed/,/# END dotfiles-managed/d')"

kept=$(printf '%s\n' "$preserved" | grep -cvE '^\s*(#|$)' || true)
echo "crontab: preserving $kept unmanaged job(s), refreshing the dotfiles block"

{ printf '%s\n' "$preserved" | sed '/^$/d'; cat "$MANAGED"; } | crontab -
