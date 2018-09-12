
# Aliases for terminal ease of use
alias ll="ls -al"
alias ls="ls -GFh"
alias cl="clear"
alias tf="terraform"
alias py2="python"
alias py3="python3"

#Functions for terminal ease of use
#Function to 'ls' immediately following 'cd'
function cd {
    builtin cd "$@" && ls -F
    }

# Colors for Terminal
export PS1='> '
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad# color scheme for Mac Terminal

