============
Python 3.6 Boilerplate
============
The best practice and standard infrastructure for starting a Python 3.6 project.

***************
Package Manager
***************
The **scripts/** folder contains a script that helps to manage your new package.

Running the command:

  ``./scripts/run.py [SCRIPT NAME]``

Will run the preffered implementation of standard-action. All of these
standard-actions are stored as functions in the run.py file where you can setup
a custom behavior for your own needs.

1. **setup:** Runs a script that initializes the boilerplate (See more below).
2. **install:** Runs a script that install required dependencies for either a
developer or user.
3. **lint:** Runs preffered linting system, defaulting to pylint using
.pylintrc.
4. **start:** Performs standard demo operation whatever that standard
implementation may be.
5. **docs:** Generates automated documentation.
6. **template:** Creates a boilerplate package or module (See more below).

The purpose of the manager is to standardize usage between Python projects which
is currently quite lacking.

***************
Setup
***************
Running the setup script will rename the main package folder, the main package
folder, and adds a PACKAGE constant into the constants.py folder.

It will also run the install script in **develop** mode to install all
dependencies. 

***************
Template Generation
***************
Templates are generated based on the **templates/** directory. You can use the
default templates which include **package** and **module**. Additional templates
can be added by adding a file or directory which will be added to the options
list when you run the script:

``./scripts/run.py template``
