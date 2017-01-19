#!/bin/bash

# Change Working Directory
dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $dir

# Setup Virtual Environment
sudo apt-get install -y python3-venv
python3 -m venv ../

# Install Dependencies
echo -n "Are you a user or developer? (common/develop): "
read environment
sudo pip3 install -r "../requirements/$environment.txt"
