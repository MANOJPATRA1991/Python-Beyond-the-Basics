"""
Using packages to structure our code

Python's basic tool for organizing the code is module 

A module typically corresponds to a single source file and we load modules into programs by using the 
*import* keyword

type(my_module) => <class 'module'>

Package in Python can contain other modules including other packages. So, packages are a way to define hierarchies of modules in Python. Allows us to group modules with similar functionalities.
"""
import urllib
import urllib.request

type(urllib)
# => <class 'module'>

type(urllib.request)
# => <class 'module'>

urllib.__path__
# => ['/usr/local/lib/python3.6/urllib']

# urllib.request.__path__
# Traceback (most recent call last):
#   File "python", line 1, in <module>
# AttributeError: module 'urllib.request' has no attribute '__path__'

"""
As urllib.request does not have a __path__ attribute, we can infer that it is a module and thus, urllib is a package.
 
Packages => Directories
Modules => Files
"""

"""
*How Python locates modules?*

sys.path => List of directories Python searches for modules
"""

import sys
sys.path
# => ['/run_dir', '/run_dir/customize', '/usr/local/lib/python36.zip', '/usr/local/lib/python3.6', '/usr/local/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages', '/home/runner/.site-packages']

"""
sys.path[0]
=> ''
This happens when we start Python with no arguments
and this instructs Python to search for modules first in the current directory

To add a module to sys.path simply append(), but a better way of doing it is with PYTHONPATH. 

PYTHONPATH  => 

Environment variable listing paths that are added to sys.path when Python starts

For Windows: ; separated list of directories

__init__.py => package init file 
This file wil make the package a module
"""

import reader.reader as reader
# reader is being imported

type(reader)
# => <class 'module'>

reader.__file__ # Source file
# => 'not_searched/reader/__init__.py'

reader.reader.__file__
# => 'organizing_larger_programs/reader/reader/reader.py'

r = reader.Reader('organizing_larger_programs/reader/reader.py')
r.read() # Prints content of the file as a string
r.close() # Closes the file

"""
absolute imports --> imports which use a full path to the module

Example: from reader.reader import Reader

relative imports --> imports which use a relative path to modules in the same package

Each dot represents a containing package

Example: from .reader import Reader

from .b import B --> one dot means same directory

from ..a import A --> two dots mean parent directory

Advantages of relative imports:

1. Can reduce typing in deeply nested package structures

2. Promote certain forms of modifiability -- we can rename top-level packages without affecting the imports

3. Can aid package renaming and refactoring

HOWEVER, RELATIVE IMPORTS ARE GENERALLY AVOIDED IN MOST CASES
"""

"""
__all__ --> 

1. list of attribute names (strings) imported via `from module import *`. If not specified, then `from module import *` imports all public names from the imported module

2. Useful tool to limit what names can be exposed from our modules

NOT RECOMMENDED: from module import *
"""

"""
What is a namespace package?

A namespace package is a package spread over several directories.

No __init__.py --> Can't have package level initialization code. Nothing will be executed by the package when it's imported. This is done to avoid complex questions of initialisation order when multiple directories contribute to a package.



How importing namespace packages work?

1. Python scans all entries in sys.path.

2. If a matching directory with __init__.py is found, a normal package is loaded.

3. If not, it checks if a file with the name is found, then it is loaded.

4. Otherwise, all matching directories in sys.path are considered part of the namespace package. 
"""
import sys
sys.path.extend(['path1', 'path2'])

import split_farm # path1 and path2 (more than one path) both match the import request, so, namespace is created

split_farm.__path__
# => _NamespacePath(['path1/split_farm', 'path2/split_farm'])

import split_farm.bird
import split_farm.bovine

split_farm.bird.__path__
# => ['path2/split_farm/bird']

split_farm.bovine.__path__
# => ['path1/split_farm/bovine']

"""
Executable directories -->

Directories containing an entry point for Python execution

To run (example):

python3 reader test.gz
"""

"""
Executable zip file --> 

Zip file containing an entry point for Python execution

To zip a file (example):

cd reader
zip -r ../reader.zip *

python3 reader.zip test.gz
"""
