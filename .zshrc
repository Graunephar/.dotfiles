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

plugins=(git firebase)



# Customize to your needs...

#Autosuggestions
#https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

#PYTHON ENV fior pycharm
export PATH="$PATH:/Users/au479136/Library/Python/2.7/bin"

#Composer for laravel
#export PATH="$PATH:$HOME/.composer/vendor/bin"
alias composer="php /usr/local/bin/composer"
#export PATH="/usr/local/opt/php@7.2/bin:$PATH"
#export PATH="/usr/local/opt/php@7.2/sbin:$PATH"


####### CUSTOM STUFF (old bashrc) 

# Brew 
export PATH=/opt/homebrew/bin:$PATH

#load custom python dir
export PATH=~/.dotfiles/python:$PATH



#Aliaser
#Aliaser
alias person="man"
alias p="pwd"

alias myip="ipconfig getifaddr en0"



#Disable autocorrect

alias npm='nocorrect npm' 
alias ruby='nocorrect ruby'
alias sass='nocorrect sass' 
 

fpath=(~/.dotfiles/zsh_fath_dir $fpath)





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

#Load a locale bin directory with all the local bin stuff
export PATH=~/bin:$PATH



#GraalVM
#export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
#export PATH=$JAVA_HOME/bin:$PATH

#More graal for Tortoise (netlogo-web)
#GRAAL_HOME='/Library/Java/JavaVirtualMachines/graalvm-ce-1.0.0-rc12/Contents/Home'
#GRAAL_HOME='/Library/Java/JavaVirtualMachines/graalvm-ce-19.0.2/Contents/Home/'


#Android
export PATH=$PATH:~/Library/Android/sdk/platform-tools/

#the fuckm autocorrect
eval $(thefuck --alias)


#Grineren


# NEXT: Lets generate an ASCII picture of a cow saying a random quote
cowsay $(quotecookie.py)




#Doing all the git related stuff
source ~/.dotfiles/git/git_custom.sh



#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/danielgraungaard/.apps-and-alike/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/danielgraungaard/.apps-and-alike/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/danielgraungaard/.apps-and-alike/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/danielgraungaard/.apps-and-alike/google-cloud-sdk/completion.zsh.inc'; fi
