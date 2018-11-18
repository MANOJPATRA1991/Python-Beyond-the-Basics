# Strings and Representations

Functions for making string representations of objects:

	1. str()
	2. repr()

These two functions depend on `__str__()` and `__repr__()` definitions inside a class to generate the strings they produce.

### repr()

* `repr()` produces an unambiguous string representation of an object.

* *unambiguous* means the string should include the type of the object and any identifying fields.

* `repr()` should contain more information than `str()`

* For easy understanding: `repr()` is for developers whereas `str()` is for clients

* Always write the `__repr()__` for a class. The default `__repr__()` represents the class name and the ID of an object.

* `repr()` is used when showing elements of a collection

* Always implement `__repr__()` for our classes as the default is not very useful.

To summarize, `repr()` is useful for:
    1. Exactness is more important than human-friendliness
    2. Suited for debugging
    3. Includes identifying information
    4. Generally best for logging

### str()

* `str()` produces readable, human-friendly representation of an object

* `str()` is the constructor for the **str** type

* `print()` uses the `str()` representation

* If `__str__()`  is not defined for a class, then `__str__()` will use `__repr__()` for its string representation. But the reverse is not true.

* `format()` replaces the `{}` with whats returned by `__format__()` method. Defaults to value returned by `str()`.

* `'{!r}'.format()` => repr representation

* `'{!s}'.format()` => str representation

### Reprlib

* If `reprlib.repr()` is used instead of `repr()` to print a very large list, it will print only a limited number of elements.

* It is useful for string representation of large collections

* `reprlib.Repr` is the main class of the `reprlib` package which implements the main function for `reprlib`. Functions from this module can be customized through subclassing.

### BUILT IN STRING FUNCTIONS

1. `ascii()`: converts non-ascii characters to escape sequences

2. `ord()`: converts a single character to its integer Unicode code point

3. `chr()`: converts an integer Unicode code point to a single character string

# Summary

* Python has two primary string representation methods: `str(obj)` and `repr(obj)`

* `__repr__(self)` should produce an unambigious, precise representation of an object, which should include type and any other identifying information. For developers.

* You should always implement `__repr__()` for your classes

* Default `__repr__()` is not very useful

* `__str__(self)` is for human consumption; doesn't need to be too precise. Has fallback to `repr()`

* `"{:f}".format(obj)` calls `__format__(self, f)`. Falls back to `str()`

* `reprlib` provides a drop-in replacement for `repr()` which limits output size

* `reprlib` is useful for printing large data structures

* `reprlib` implements the class `Repr`

* `reprlib.Repr` is designed to be extended and customized via inheritance

* `ascii(string)` replaces non-ASCII characters in a Unicode string with escape sequeunces

* `ord()` takes a single character Unicode string and converts it to a Unicode codepoint

* `chr()` reverse the ord() (inverses of one another)

* Good `__repr__` functions are easy to write and can improve debugging and reporting errors