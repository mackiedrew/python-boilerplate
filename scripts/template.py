#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This template generater can be used to copy directories of templates to new
locations to facilitate simple boilerplated-files.
'''

# Standard Imports
from os import chdir, listdir
from os.path import isfile
from shutil import copytree, copy2

# Constants
WORKING_DIRECTORY = '../'
TEMPLATE_DIRECTORY = 'templates/'
SOURCE_DIRECTORY = 'src/'

# Function Declarations
def copy_anything(path, destination):
    '''Determines best practice for copying a path and will do it's best
    to make it happen.'''
    path_is_file = isfile(path)
    print(path_is_file)
    print(path)
    print(destination)
    if path_is_file:
        copy2(path, destination)
    else:
        path_root = path.split('/')[-1]
        destination += path_root
        copytree(path, destination)

def raw_file(file_name):
    '''Remove extension for file_name.'''
    return file_name.split('.')[0]

def raw_dir(directory):
    '''Remove forward slash from directory.'''
    return directory.strip('/')

def list_templates(path=TEMPLATE_DIRECTORY):
    '''Collect list of simple template names (key) added with true directory.'''
    listings = listdir(path)
    full_listings = [path + listing for listing in listings]
    is_files = [isfile(listing) for listing in full_listings]
    simple_names = [raw_file(listing) if is_file else raw_dir(listing)
                    for is_file, listing in zip(is_files, listings)]
    templates = {name: listing
                 for name, listing in zip(simple_names, full_listings)}
    return templates

def create_template(template, directory):
    '''Copy a template from a template folder to the src destination.'''
    destination_path = SOURCE_DIRECTORY + directory + '/'
    copy_anything(template, destination_path)

def main():
    '''Run through template generation main process.'''
    chdir(WORKING_DIRECTORY)
    templates = list_templates()
    template_names = str('/'.join(templates.keys()))
    template_message = "Enter template type (%s): " % (template_names)
    template_input = input(template_message)
    template = templates[template_input]

    directory_message = "Which directory? %s" % SOURCE_DIRECTORY
    directory = input(directory_message)

    create_template(template, directory)

if __name__ == '__main__':
    main()
