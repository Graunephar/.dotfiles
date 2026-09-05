# Host profiles

Per-machine config layered on top of the shared setup, so one branch serves
every Mac. No branch-per-machine, no merging.

## How it works

`./install` runs dotbot twice:

1. `install.conf.yaml` — the shared config, applied on every machine.
2. `hosts/<LocalHostName>.conf.yaml` — this machine only, applied on top.

The host name comes from:

```bash
scutil --get LocalHostName
```

A machine with no matching file simply gets the shared config. Nothing breaks,
it just installs less.

Each host profile links `~/.dotfiles-host` to its own directory. The shared
`zsh/zshrc` ends with:

```zsh
[[ -f ~/.dotfiles-host/zshrc.local ]] && source ~/.dotfiles-host/zshrc.local
```

so one shared line gives every machine its own shell config.

## Adding a machine

```bash
HOST=$(scutil --get LocalHostName)
mkdir -p "hosts/$HOST"
cp hosts/Daniels-Mac-Studio.conf.yaml "hosts/$HOST.conf.yaml"
cp hosts/Daniels-Mac-Studio/zshrc.local "hosts/$HOST/zshrc.local"
```

Then edit both files and replace `Daniels-Mac-Studio` with the new host name in
the `link:` path.

## mackup: one writer

mackup has no conflict resolution. Two machines backing up to one folder means
last-write-wins, and the older config silently destroys the newer one. That is
not theoretical - on 2026-09-05 the Studio's agent overwrote the MacBook's
BetterTouchTool config within minutes of being enabled.

So the backup agent lives in the **MacBook's** profile only. The Studio restores
with `mackup-pull <app>` (defined in its `zshrc.local`) and never writes.

Revisit once the Studio holds config worth keeping. The upgrade path is a
staleness guard in `misc/mackup-backup.sh`: refuse to back up when storage is
newer than local. Then both machines can write safely.

## What belongs here — and what does not

Default to the **shared** config. Reach for a host profile only when something:

- costs shell-startup time on a machine that does not need it,
- runs a background daemon that machine should not run, or
- is genuinely broken or unavailable there.

Disk space alone is not a reason. A CLI tool sitting unused costs nothing at
runtime, and duplicating config across profiles is how two machines silently
drift apart.

If you are unsure: shared. Moving something into a profile later is easy;
finding out months on that your two Macs disagree is not.

## Current machines

| Host name (`LocalHostName`) | Machine | Role |
|---|---|---|
| `Daniels-Mac-Studio` | Mac Studio, M4 Max, 36 GB | AI work engine. Kept lean. **Reads mackup only** - use `mackup-pull <app>`. |
| `Daniels-MacBook-Pro-2` | MacBook Pro | Everyday machine, full setup. **Single writer for mackup** - runs the 3-hourly backup agent. |

To add the MacBook, run `scutil --get LocalHostName` on it and follow
"Adding a machine" above.
