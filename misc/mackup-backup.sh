#!/usr/bin/env bash
# Daily mackup backup, run by launchd.
#
# Backup only. Restore stays manual on purpose: two machines auto-restoring
# from the same folder would fight, and whichever ran last would win.
#
# Logs to ~/Library/Logs/mackup-backup.log so a silent failure is visible.
# The old cron job failed silently for ~3 years - every ~/Library path denied
# because cron lacked Full Disk Access - and nothing surfaced it. Hence the log
# and the explicit exit-code check below.
set -uo pipefail

LOG="$HOME/Library/Logs/mackup-backup.log"
MACKUP="$(command -v mackup || echo /opt/homebrew/bin/mackup)"

exec >>"$LOG" 2>&1
echo "=== $(date '+%Y-%m-%d %H:%M:%S') starting on $(scutil --get LocalHostName 2>/dev/null || hostname -s) ==="

[ -x "$MACKUP" ] || { echo "ERROR: mackup not found"; exit 1; }
echo "using $MACKUP ($("$MACKUP" --version 2>&1))"

# Storage must exist, or mackup happily "succeeds" while writing nowhere.
STORAGE="$HOME/$(awk -F= '/^path/{gsub(/ |#.*/,"",$2); print $2}' "$HOME/.mackup.cfg" 2>/dev/null)"
if [ ! -d "$STORAGE/Mackup" ]; then
  echo "ERROR: storage $STORAGE/Mackup missing - is the cloud folder synced?"
  exit 1
fi

"$MACKUP" backup -f
rc=$?
echo "mackup exited $rc"

# Prove it actually wrote something. `find -mtime` is unreliable across the
# File Provider mount, so stat a file mackup always touches and compare epochs.
probe="$STORAGE/Mackup/Library/Preferences/com.googlecode.iterm2.plist"
if [ -f "$probe" ]; then
  age=$(( $(date +%s) - $(stat -f %m "$probe") ))
  if [ "$age" -lt 900 ]; then
    echo "OK: storage written ${age}s ago"
  else
    echo "WARNING: newest write is ${age}s old - backup may be failing silently"
  fi
else
  echo "WARNING: probe file missing from storage"
fi
exit $rc
