#!/bin/bash

# Change Working Directory
dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $dir

# Setup Virtual Environment
sudo wget "https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh"
bash Miniconda3-latest-Linux-x86_64.sh
sudo rm Miniconda3-latest-Linux-x86_64.sh
~/miniconda3/bin/conda update conda

# Install Dependencies
~/miniconda3/bin/conda env create -n pycast_env --file "../requirements/environment.yml"
