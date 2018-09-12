# This program will use the MAC OS syntax wrapped in python to create a boilerplate that can be used to configure
# any MAC to a suitable environment for my requirements

import os 

print("MAC_Boiler Initialized...")
print(os.getcwd())
print("Verifiying ~/.bash_profile exists...")

# if file exists :
#     #Print exists here...
# else :
#     #Print doesn't exist and create

# Update ~/.bash_profile with code here
# alias ll=‘ls -al’
# alias ls=‘ls -GFh’
# alias cl=‘clear’
# alias tf=‘terraform’
# alias py2=‘python’
# alias py3=‘python3’

# Install homebrew
os.system("/usr/bin/ruby -e '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)'")
os.system("brew analytics off")

# Install Git
os.system("brew install git")

# Install Terraform
os.system("brew install Terraform")

# Install Pythonn3
os.system("brew install git")

# Install AWS CLI
os.system("curl 'https://s3.amazonaws.com/aws-cli/awscli-bundle.zip' -o 'awscli-bundle.zip'")
os.system("unzip awscli-bundle.zip")
os.system("sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws")

# Install VSCode
os.system("brew install visual-studio-code")

# Install Ansible
os.system("brew install Ansible")

# Install WGET
os.system("brew install wget")

# Install HTOP
os.system("brew install htop")

# Install Tree
os.system("brew install tree")