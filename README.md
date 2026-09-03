# Graunephars .dotfiles

All of my .dotfiles will eventually be collected here. Mostly for my own reference. 

But you are more than welcome to have a look and copy the things you like.

## General setup

I run a Oh My Zsh Terminal with a heavily customized version of the [powerlevel10k](https://github.com/romkatv/powerlevel10k) theme. The font is MesloLGS NF. 

### System types

At the moment most of the things are only used on macs. Although I have some branches that I have used in the past for specifik linux machines. 
That way changes can be merged to specific machines. 
However my long term plan is to include linux in the main branch. Making a setup were as much as possible can be synced between machines. 

The repo uses [dotbot](https://github.com/anishathalye/dotbot) to handle installation

# Mac Setup

I use Mackup and dotbot to transfer settings between macs. Mackup stores its folder in **Proton Drive**, not in this repo, so that sensitive files never reach GitHub by mistake. Proton mounts through macOS File Provider, so the path under `~/Library/CloudStorage/` is the same on every Mac signed into the account.

Note: Mackup 0.11 changed its defaults — `backup`/`restore` now **copy** files. The old symlink behaviour is opt-in via `mackup link install` / `mackup link` / `mackup link uninstall`.
$
Keyboard Maestro and BetterTouchTool sync their own settings into the same Proton `Sync/` folder, separately from Mackup — Mackup holds only dotfiles, so the two never collide.


## Installation

Make sure Proton Drive is installed and the `Sync/Mackup` folder has synced down before running ./install — otherwise `mackup restore` silently does nothing.

run ./install to install all the things on a mac 

# manual setup
Keyboard Maestro and BetterTouchTool sync their own settings and must be pointed at the files in Proton `Sync/` by hand on a new machine:

- Keyboard Maestro -> `Sync/Keyboard Maestro Macros.kmsync`
- BetterTouchTool -> `Sync/Default.bttpreset`


## Core settings on mac

- iTerm2 - The colors in iTerm is the Night Owl theme with some slight modifications.
- Keyboard Maestro
- Karabiner (with Goku)
- Better Touch Tool
- ~~Alfred settings including workflows.~~ Currently trialling life without Alfred. `Sync/Alfred/` is kept as reference for configuring a replacement launcher.

# Linux setup

Next step is to write a seperat script that can install most of the setup on an ubuntu based system as well.
