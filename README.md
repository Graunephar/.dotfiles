# Graunephars .dotfiles

All of my .dotfiles will eventually be collected here. Mostly for my own reference. 

But you are more than welcome to have a look and copy the things you like.

## General setup

I run a Oh My Zsh Terminal with a heavily customized version of the [powerlevel10k](https://github.com/romkatv/powerlevel10k) theme. The font is MesloLGS NF.

Note that MesloLGS NF is not the same as the `font-meslo-lg-nerd-font` cask. That one installs a font called "MesloLGS Nerd Font", which is a different name, so my iTerm profiles don't match it and iTerm quietly falls back to something else with broken p10k icons. The install downloads the right one from romkatv directly.

The repo uses [dotbot](https://github.com/anishathalye/dotbot) to handle installation

### How it all fits together

Two things carry my config between machines, and they hold different stuff:

**This git repo** — shell config, karabiner.edn, git config, scripts, the install itself. It's public, so nothing sensitive goes in it. `./install` links it all into place with dotbot.

**A private repo** — the app settings that can't live in a public repo: iTerm, Keyboard Maestro, BetterTouchTool and so on. Mackup's storage lives there, with anything sensitive encrypted at rest via git-crypt. It used to be cloud storage, which is why the old `mackup.cfg` pointed at a `Sync/` folder that hadn't existed for years.

**A skills repo** — [github.com/Graunephar/skills](https://github.com/Graunephar/skills), my own Claude skills. Public on purpose: they're mine to give away, and its README collects other people's skills I like. Skills I install from elsewhere, and the private ones, stay in the mackup repo instead.

So: **public repo for anything I'd show people, private repo for everything else.** The private repo has to be cloned and unlocked before `./install` is worth running, or mackup has nothing to read.

On top of that, two rules keep the two macs from fighting:

- **Host profiles** decide what each machine installs — see below.
- **Only the MacBook writes to the mackup repo.** The Studio reads. Mackup has no conflict resolution of its own, so two writers means trusting git to catch what mackup won't.

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

I use Mackup and dotbot to transfer settings between macs. Mackup stores its folder in **a private repo**, not in this one, so nothing sensitive lands in a public repo by mistake.

It used to live in cloud storage, and must never go back. Cloud drives mount through macOS File Provider, which only exists inside a logged-in user session — so root daemons can't read those paths at all. Karabiner's `core_service` runs as root, silently failed to load its config from there, and fell back on a years-old system copy. Every keybinding died, with nothing but a line in `/var/log/karabiner/core_service.log` to say why. A repo on ordinary disk doesn't have that problem.

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
- stops if the mackup folder isn't there, instead of "succeeding" while writing nowhere
- checks after each run that something was actually written, and says `WARNING` if not
- runs a missed job when the mac wakes up, which cron doesn't

If it logs `WARNING`, that machine probably needs Full Disk Access for `/bin/zsh`.

## Claude skills come from two repos

`~/.claude/skills` holds every skill, but nothing actually lives there — mackup
owns that folder and links it at the mackup store. The skills themselves sit in
one of two repos, and both are a source of truth:

| Where | What | Visibility |
|---|---|---|
| `~/Git/skills` | skills I wrote | public |
| mackup store, `.claude/skills/` | skills I installed, and private ones | private, git-crypt |

The trick is that the store contains a **symlink** for each skill in the public
repo, pointing back at `~/Git/skills/<name>`. Git stores symlinks as symlinks, so
the link survives a clone, and both machines have the same username and so the
same absolute path.

That means a skill exists in exactly one repo. Write one in `~/Git/skills` and it
reaches the other mac through that repo; install one and it reaches the other mac
through the mackup repo. Neither can drift from the other, because there is no
second copy to drift.

`./install` clones the public repo if it's missing and creates any symlink that
isn't there yet. It only ever adds. Deleting a skill from the public repo leaves
a broken symlink in the store on purpose — an install script that deletes files
in the encrypted store is the one mistake with no undo.


## Custom mackup app definitions

`mackup/bettertouchtool.cfg` gets linked to `~/.mackup/bettertouchtool.cfg`, where mackup lets custom definitions override its own.

Mackup's built-in BetterTouchTool definition points at `bttdata2` and `btt_data_store.v2`. BTT hasn't used those names for years — it writes `btt_data_store.version_<version>_build_<date>`, which changes on every update. So the built-in definition matched nothing and only ever backed up the plist. That's why my triggers were never synced. Mine targets the folder instead, so it survives updates.

## Installation

The private mackup repo has to be cloned and unlocked with git-crypt before running ./install, otherwise mackup has nothing to work with. Clone it to ordinary disk — never into a cloud-synced folder.

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

# Linux setup

Next step is to write a seperat script that can install most of the setup on an ubuntu based system as well.
