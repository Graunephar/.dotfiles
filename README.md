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

I use Mackup and dotbot to tranfer settings between macs. At the moment Mackup backs up to an external file storage service. This is mainly because I am afraid that I will sync some sensitive information to github by mistake. 
$
Both keyboard Meastro and ALfred fuirthermore syncs their settings themselves to a third part file service. 


## Installation

Make sure that th Mackup folder is located in the folder described in mackup.cfg (by asking the cloud provider to sync it to that folder)

run ./install to install all the things on a mac 

# manual setup
Both Alfred and Keyboard Meastro is setup to sync there own settings manually (as a failsafe just to be sure. So set this sync up again)


## Core settings on mac

- iTerm2 - The colors in iTerm is the Night Owl theme with some slight modifications.
- Keyboard Maestro
- Karabiner (with Goku)
- Better Touch Tool
- Alfred settings including workflows.

# Linux setup

Next step is to write a seperat script that can install most of the setup on an ubuntu based system as well.
