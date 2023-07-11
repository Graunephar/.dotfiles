
# function mkdir {
#   if [ ! -n $1 ]; then
#     echo "Enter a directory name"
#   elif [ -d $1 ]; then
#     echo "$1 already exists"
#   else
#     command mkdir $1 && cd $1
#   fi
# }

## update mkdir so we automatically steps into new directories
#function mkdir {
#    command mkdir $1 && cd $_
#}

# use colorls for plain ls. Use plain ls for everything with arguments
function ls {
    if [ $# -gt 1 ]; then # split if arguments
        command ls $@ # the command command fixes recursive problem: https://stackoverflow.com/questions/68223884/fish-how-to-prevent-recursive-function-calls
    else # there was no arguments
        colorls
    fi
}

command_not_found_handler() {
    echo $c[red] $c[bold]  "🤷️: $@" $c[reset]
    return 127
}

# Demo of how to pass variables when wriding my own functions in shell
testfunctiondemo(){
   # t stores $1 argument passed to fresh()
   t=$1
   echo "fresh(): \$0 is $0"
   echo "fresh(): \$1 is $1"
   echo "fresh(): \$t is $t"
   echo "fresh(): total args passed to me $#"
   echo "fresh(): all args (\$@) passed to me -\"$@\""
   echo "fresh(): all args (\$*) passed to me -\"$*\""
}
