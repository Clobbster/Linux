# This program will use the MAC OS syntax wrapped in python to create a boilerplate that can be used to configure
# any MAC to a suitable environment for my requirements

import os

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