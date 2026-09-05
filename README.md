# Graunephars .dotfiles

All of my .dotfiles will eventually be collected here. Mostly for my own reference. 

But you are more than welcome to have a look and copy the things you like.

## General setup

I run a Oh My Zsh Terminal with a heavily customized version of the [powerlevel10k](https://github.com/romkatv/powerlevel10k) theme. The font is MesloLGS NF.

Note that MesloLGS NF is not the same as the `font-meslo-lg-nerd-font` cask. That one installs a font called "MesloLGS Nerd Font", which is a different name, so my iTerm profiles don't match it and iTerm quietly falls back to something else with broken p10k icons. The install downloads the right one from romkatv directly.

The repo uses [dotbot](https://github.com/anishathalye/dotbot) to handle installation

### System types

At the moment most of the things are only used on macs. Although I have some branches that I have used in the past for specifik linux machines. 
That way changes can be merged to specific machines. 
However my long term plan is to include linux in the main branch. Making a setup were as much as possible can be synced between machines. 

### Host profiles

For the two macs I don't use branches. `./install` runs dotbot twice: first the shared `install.conf.yaml`, then `hosts/<LocalHostName>.conf.yaml` if there is one. So both machines run off the same branch and I never have to merge anything between them.

A machine with no profile just gets the shared config. Nothing breaks, it only installs less.

Each profile links `~/.dotfiles-host` to its own folder, and the shared zshrc ends by sourcing `~/.dotfiles-host/zshrc.local`. That way one line in the shared file gives every machine its own tail.

See `hosts/README.md` for how to add a machine. Default to putting things in the shared config — a profile is for things that cost startup time, run a daemon, or are actually broken on the other machine. Not for things I just don't happen to use there.

# Mac Setup

I use Mackup and dotbot to transfer settings between macs. Mackup stores its folder in **Proton Drive**, not in this repo, so I don't sync anything sensitive to github by mistake. Proton mounts through macOS File Provider, so the path under `~/Library/CloudStorage/` is the same on every mac signed into the account. Before that it was pCloud, and sync.com before that.

Note: Mackup 0.11 changed its defaults. `backup` and `restore` now **copy** files. The old symlink behaviour is opt-in with `mackup link install` / `mackup link` / `mackup link uninstall`. Both machines need to be on 0.11 or they disagree about what a backup even is.

## Only one machine backs up

Mackup has no conflict resolution. If both machines back up to the same folder it's last-write-wins, and the older config silently destroys the newer one. That is not theoretical — I turned the agent on on both machines and within minutes the Studio had overwritten the MacBook's BetterTouchTool config.

So:

- **MacBook is the writer.** It runs the backup agent, every 3 hours.
- **Mac Studio only reads.** It has a `mackup-pull <app>` function in its `zshrc.local`. Quit the app, pull, relaunch.

The agent is linked from the MacBook's host profile only, so running `./install` on the Studio can't accidentally make it a writer. Same goes for any mac I set up later — no profile means no agent, so a new machine reads and never writes until I decide otherwise. That's the point of keeping the agent in a profile instead of the shared config: the rule is enforced by the setup, not by me remembering it.

If the Studio ever holds config worth keeping, the way out is a staleness check in `misc/mackup-backup.sh`: refuse to back up when the folder is newer than local. Then both can write.

Restore is deliberately not automated. It overwrites config files, and a running app writes its own back out when it quits, so it has to be done with the app closed.

## The backup agent

`misc/dk.graunephar.mackup-backup.plist` + `misc/mackup-backup.sh`, loaded through launchd.

This used to be a cron job. It stopped working around March 2023 and I didn't notice until September 2026, when I set up the Studio and found BetterTouchTool still on a preset from 2019 and iTerm on one from 2022. Cron on modern macOS has no Full Disk Access, so every `~/Library` path was denied, and cron's output goes nowhere, so nothing ever told me.

The launchd version therefore:

- logs every run to `~/Library/Logs/mackup-backup.log` (`mackup-log` on the MacBook)
- stops if the Proton folder isn't there, instead of "succeeding" while writing nowhere
- checks after each run that something was actually written, and says `WARNING` if not
- runs a missed job when the mac wakes up, which cron doesn't

If it logs `WARNING`, that machine probably needs Full Disk Access for `/bin/zsh`.

## Custom mackup app definitions

`mackup/bettertouchtool.cfg` gets linked to `~/.mackup/bettertouchtool.cfg`, where mackup lets custom definitions override its own.

Mackup's built-in BetterTouchTool definition points at `bttdata2` and `btt_data_store.v2`. BTT hasn't used those names for years — it writes `btt_data_store.version_<version>_build_<date>`, which changes on every update. So the built-in definition matched nothing and only ever backed up the plist. That's why my triggers were never synced. Mine targets the folder instead, so it survives updates.

## Installation

Proton Drive has to be installed and `Sync/Mackup` synced down before running ./install, otherwise mackup has nothing to work with.

run ./install to install all the things on a mac 

# manual setup

Keyboard Maestro syncs its own settings, separate from Mackup, so it has to be pointed at the file by hand on a new machine:

- Keyboard Maestro -> `Sync/Keyboard Maestro Macros.kmsync`

Use **Open**, not Create. Create writes the new machine's empty macro set into the file and syncs that everywhere.

The setting is under Settings -> General -> Sync Macros. It's stored as a security-scoped bookmark, so it can't be scripted or set with `defaults` — it has to go through the file dialog.

If Keyboard Maestro was launched from Downloads instead of /Applications, macOS runs it translocated from a read-only path and the setting won't stick. Move the app first.

BetterTouchTool used to be in this list. It goes through Mackup now, see above.

## Core settings on mac

- iTerm2 - The colors in iTerm is the Night Owl theme with some slight modifications.
- Keyboard Maestro
- Karabiner (with Goku)
- Better Touch Tool
- ~~Alfred settings including workflows.~~ Currently trialling life without Alfred. `Sync/Alfred/` is kept as reference for configuring a replacement launcher.

# Linux setup

Next step is to write a seperat script that can install most of the setup on an ubuntu based system as well.
