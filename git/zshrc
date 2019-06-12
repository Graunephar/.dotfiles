#
# Executes commands at the start of an interactive session.
#
# Authors:
#   Sorin Ionescu <sorin.ionescu@gmail.com>
#

# Source Prezto.
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi

# Customize to your needs...



####### CUSTOM STUFF (old bashrc) 

#Aliaser
alias pdf=evince


#Disable autocorrect

alias npm='nocorrect npm' 
alias ruby='nocorrect ruby'
alias sass='nocorrect sass' 
 




#Doing all the git related stuff
source ~/.git_custom.sh

# update mkdir so we automatically steps into new directories
function mkcd {
  if [ ! -n "$1" ]; then
    echo "Enter a directory name"
  elif [ -d $1 ]; then
    echo "\`$1' already exists"
  else
    mkdir "$1" && cd "$1"
  fi
}

# auto-completion
if [ -f /opt/local/etc/profile.d/bash_completion.sh ]; then
  . /opt/local/etc/profile.d/bash_completion.sh
fi

#Dangarous stuff, when you want it ask first
function ask() {

	read -p "$1" -n 1 -r
	echo    # (optional) move to a new line
	if [[ $REPLY =~ ^["$2"]$ ]]
	then
	    return 0
	fi
	return 1

}

#Grineren


# NEXT: Lets generate an ASCII picture of a cow saying a random quote
cowsay $(fortune)
