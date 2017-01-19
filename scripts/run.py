#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The purpose of this script is to run standard maintanence scripts that may be
involved in development or use. This is intended to recreate the standardized
operation of packages used by NPM in JavaScript development.
'''

# Standard Imports
from os import system, chdir
from os.path import abspath, dirname
from argparse import ArgumentParser

# Function Declarations
def home():
    '''Change the working directory to this scripts location.'''
    this_file = __file__
    absolute_path = abspath(this_file)
    directory = dirname(absolute_path)
    chdir(directory)

def run(command):
    '''Runs a terminal command.'''
    system(command)

def install():
    '''Installs all dependencies required for using PyCast.'''
    run('./install.sh')

def start():
    '''Standard demo operation for running the script. May have a package-
    specific implementation.'''
    pass

def lint():
    '''Checks for style consistency.'''
    run('pylint --rcfile=../.pylintrc ../src/')

def docs():
    '''Regenerate documentation for specified source.'''
    pass

def template():
    '''Use a template generation script to create code snippets.'''
    run('python3 template.py')

def main():
    '''Switches to a script to run.'''
    # Configure argument parser
    parser = ArgumentParser(description="Runs a maintaining script of choice.")
    parser.add_argument('script', help="Select script name to run.")

    # Extract arguments from argument parse
    args = parser.parse_args()
    script = args.script

    # Configure Environment
    home()

    # Select script
    scripts = {
        'install': install,
        'start': start,
        'lint': lint,
        'docs': docs,
        'template': template,
        }

    # Run selected script
    scripts[script]()

# Main body
if __name__ == '__main__':
    main()
