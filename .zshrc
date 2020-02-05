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

#Autosuggestions
#https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh


#PYTHON ENV fior pycharm
export PATH="$PATH:/Users/au479136/Library/Python/2.7/bin"

#Composer for laravel
export PATH="$PATH:$HOME/.composer/vendor/bin"
alias composer="php /usr/local/bin/composer.phar"
export PATH="/usr/local/opt/php@7.2/bin:$PATH"
export PATH="/usr/local/opt/php@7.2/sbin:$PATH"


####### CUSTOM STUFF (old bashrc) 

#Aliaser
#Aliaser
alias person="man"
alias p="pwd"



#Disable autocorrect

alias npm='nocorrect npm' 
alias ruby='nocorrect ruby'
alias sass='nocorrect sass' 
 

fpath=(~/.dotfiles/zsh_fath_dir $fpath)



#Doing all the git related stuff
source ~/.dotfiles/git/git_custom.sh

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

#GraalVM
#export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
#export PATH=$JAVA_HOME/bin:$PATH

#More graal for Tortoise (netlogo-web)
GRAAL_HOME='/Library/Java/JavaVirtualMachines/graalvm-ce-1.0.0-rc12/Contents/Home'
#GRAAL_HOME='/Library/Java/JavaVirtualMachines/graalvm-ce-19.0.2/Contents/Home/'



#Grineren


# NEXT: Lets generate an ASCII picture of a cow saying a random quote
cowsay $(fortune)
