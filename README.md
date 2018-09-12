# Mac_Boiler_Plate
# The goal of this is to take a list of typical programs that I use and generate a script that I can call from
# github to setup my environment if need be. 

# I will endeavor to ensure that I can set terminal and background settings as well if possible. 

Mac Init:

# The following are things that I think are important to setup initially on a Mac for usability

# Creation and configuration of a bash_profile file
1. Mkdir ~/.bash_profile
2. Nano ~/.bash_profile
3. alias ll=‘ls -al’
4. alias ls=‘ls -GFh’
5. alias cl=‘clear’
6. alias tf=‘terraform’
7. alias py2=‘python’
8. alias py3=‘python3’

# Installation of homebrew
1. /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
2. Once installation is done ‘brew help’ should answer any syntax commands you may have
3. brew analytics off

# Installation of GIT
1. brew install git
2. /usr/local/Cellar/git

# Installation of Terraform
1. brew install terraform
2. /usr/local/Cellar/terraform

# Installation of Python3
1. brew install python3
2. /usr/local/bin/python3

# Installation of AWS CLI
1. curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip”
2. unzip awscli-bundle.zip
3. sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

# Installation of VSCode
1. brew cask install visual-studio-code

# Installation of Ansible
1. brew install sensible
2. /usr/local/Cellar/ansible

# Installation of wget
1. brew install wget
2. /usr/local/Cellar/wget

# Installation of HTop and Tree
1. brew install htop
2. brew install tree

