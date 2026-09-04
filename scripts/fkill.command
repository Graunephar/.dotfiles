#!/bin/sh
# Fuzzy process killer — replacement for the Alfred "Kill Process" workflow.
#
# Usage:
#   fkill [query]      pick process(es) and send SIGTERM
#   fkill -9 [query]   send SIGKILL instead
#
# TAB marks several processes, ENTER kills the marked ones.

# Homebrew is not on PATH when launched from a GUI app (RustCast, iTerm "open").
PATH="/opt/homebrew/bin:$PATH"
export PATH

sig=TERM
case $1 in
  -*) sig=${1#-}; shift ;;
esac

# -r sorts by CPU usage, so the misbehaving process floats to the top.
pids=$(ps -A -r -o pid=,%cpu=,comm= |
  fzf --multi --query="$*" --prompt='kill > ' \
      --header='TAB = mark several, ENTER = kill' |
  awk '{print $1}')

[ -n "$pids" ] || exit 0
echo "$pids" | xargs kill -"$sig"
