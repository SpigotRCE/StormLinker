#!/bin/bash

# Update package lists
sudo apt update

# Install Python 3 and pip
sudo apt install -y python3 python3-pip

# Install requests library
pip3 install requests

# Install Java Runtime Environment (JRE)
sudo apt install -y default-jre

# Install git
sudo apt install -y git

# Clone the repository
git clone https://github.com/SpigotRCE/StormLinker
