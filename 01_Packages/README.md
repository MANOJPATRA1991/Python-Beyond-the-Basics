# Summary

* Packages are a special type of modules.

* Unlike modules, packages can contain other modules including other packages

* Package hierarchy is a powerful way to organize related code

* Packages have a `__path__` attribute which is a sequence specifying the directories from which a package is loaded

* `sys.path` is a list of directories where Python searches for modules

* `sys.path` is a normal list and can be modified and queried like any other list

* If you start Python with no arguments, an empty string is put at the front of `sys.path` - this instructs Python to import a module from the current directory

* Appending directories to `sys.path` at runtime allows modules to be imported from those directories

* `PYTHONPATH` is an environment variable containing a list of directories

* The format of `PYTHONPATH` is the same as system `PATH` variable

* Contents of `PYTHONPATH` is appended to the end of `sys.path`

* Normal packages are implemented by putting a file named **__init__.py** into a directoriy

* The **__init__.py** file in a directory is executed when the package is first imported

* The **__init__.py** file can hoist attributes from sub-modules or higher namespaces for convenience

* Modules can be executed by python with the -m argument

* Relative imports allow you to import modules within a package without specifying the full module path

* Relative imports must use the from `<module>` import `<name>` form of import

* Avoid relative imports because they can make the code harder to understand

* The `__all__` attribute of a module is a list of strings specifying the names to export when `from <module> import *` is used

* A **namespace** package is a package split across several directories

* Namespace packages are described in **PEP420**

* Namespace packages don't use **__init__.py** files

* Namespace packages are created when one or more directories in the `PYTHONPATH` match an import request and no normal packages or modules match the request

* Each directory that contributes to a namespace package is listed in the packages in the `__path__` attribute

* Executable directories are executed by putting a **__main__.py** file in a directory. When **__main__.py** is executed, the `__main__` attribute is set to `__main__`, and *its parent directories are automatically added to sys.path*

* Executable directories can be compressed into .zip files, which can be executed as well

* Executable directories and zip files are convenient ways to distribute Python programs

* A simple standard project structure includes a location for non-Python files, a project package, and dedicated test subpackage

* **Module level attributes provide a good mechanism for implementing singletons**

* Modules have well defined initialization semantics