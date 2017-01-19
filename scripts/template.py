#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This template generater can be used to copy directories of templates to new
locations to facilitate simple boilerplated-files.
'''

# Standard Imports
from os import chdir
from os.path import isfile
from shutil import copytree, copy2

# Constants
WORKING_DIRECTORY = '../'
TEMPLATE_DIRECTORY = 'templates/'
SOURCE_DIRECTORY = 'src/'
PACKAGE = 'PACKAGE/'
MODULE = 'MODULE.py'

# Function Declarations
def copy_anything(path, destination):
    '''Determines best practice for copying a path and will do it's best
    to make it happen.'''
    path_is_file = isfile(path)
    print(path)
    print(destination)
    if path_is_file:
        copy2(path, destination)
    else:
        copytree(path, destination)

def create_template(template, directory):
    '''Copy a template from a template folder to the src destination.'''
    full_template_path = './' + TEMPLATE_DIRECTORY + template
    destination_path = './' + SOURCE_DIRECTORY + directory
    copy_anything(full_template_path, destination_path)

def main():
    '''Run through template generation main process.'''
    chdir(WORKING_DIRECTORY)
    templates = {
        'module': MODULE,
        'package': PACKAGE,
        }

    template_names = str('/'.join(templates.keys()))
    template_message = "Enter template type (%s): " % (template_names)
    template_input = input(template_message)
    template = templates[template_input]

    directory_message = "Which directory? %s" % SOURCE_DIRECTORY
    directory = input(directory_message)

    create_template(template, directory)

if __name__ == '__main__':
    main()
