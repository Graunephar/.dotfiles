#!/bin/zsh
# vnc-passthrough — let Hyper-chords reach the machine you're VNC'd INTO.
#
# Problem: BTT registers system-wide hotkeys. When the Screen Sharing window is
# focused, the LOCAL BTT eats e.g. Caps Lock+R (Hyper+R) and moves the Screen
# Sharing window, so the chord never forwards to the remote Mac. Karabiner can't
# fix this — global hotkeys sit above Karabiner's output.
#
# Fix: while Screen Sharing is frontmost, suspend the local grabber. The chord
# then forwards untouched, and the remote machine's own BTT (same config) acts.
#
# Safe to run on every host: if you never focus Screen Sharing, it does nothing.

TARGET_BUNDLE="com.apple.ScreenSharing"
POLL=0.4

prev=""
suspended=0

frontmost() {
  lsappinfo info -only bundleID "$(lsappinfo front)" 2>/dev/null \
    | sed -n 's/.*"CFBundleIdentifier"="\([^"]*\)".*/\1/p'
}

suspend_grabbers() {
  osascript -e 'tell application "BetterTouchTool" to quit' >/dev/null 2>&1
  suspended=1
}

resume_grabbers() {
  open -a BetterTouchTool >/dev/null 2>&1
  suspended=0
}

# Never leave BTT dead if this agent is stopped.
trap '[ "$suspended" = 1 ] && resume_grabbers; exit 0' TERM INT HUP

while :; do
  front=$(frontmost)
  if [ "$front" != "$prev" ]; then
    if [ "$front" = "$TARGET_BUNDLE" ] && [ "$suspended" = 0 ]; then
      suspend_grabbers
    elif [ "$front" != "$TARGET_BUNDLE" ] && [ "$suspended" = 1 ]; then
      resume_grabbers
    fi
    prev="$front"
  fi
  sleep "$POLL"
done
