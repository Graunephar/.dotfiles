
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


function gitrevertdangerous {

ask 'Are you sure? (y/n) ' "Yy" && ask "This will force push to the repo. Deleting the last commit entirely. Are you completely sure? (y/n) " "Yy" && ask "Every collaborator might get problems from this. If you are not collaborating with a small team you should really find another option.  Do you want to abort? (y/n) " "nN" && git reset --soft HEAD^ && git push origin +master 

}


function check_input {
	if [ -z "$1" ]
	then
	      echo "Please provide input to this command"
	      return 1
	else
	      return 0
	fi
}

