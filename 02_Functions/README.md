# Summary

* Callable objects are of four types:
  1. Functions
  2. Callable instances
  3. Lambdas
  4. Classes

* Functions are **first-class** meaning they are objects that can be passed around like any other objects.

* Two types of arguments:
  1. Positional arguments in a function call ===> formal arguments in definition in order
  2. Keyword arguments in a function call ===> keyword arguments in definition mapped by name (not by order)
    * Always come after positional arguments

* Default argument values are assigned when the `def` statement is executed first which is when the module is imported

* **Callable Instances** --> Callable instances can be used when we need to maintain state between calls and optionally need to support attributes for clearing or modifying the state

* Classes in Python are *objects* as well as *callable*.
  * Calling a class invokes its constructor `__init__()` to create a new instance

* Diiference between Normal Functions and Lambda Functions:

| Normal Functions                                                   | Lambda Functions                                                                   |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------|
|                                                                    |                                                                                    |
| A statement which defines a function and binds it to a name        | An expression which evaluates to a function object                                 |
|                                                                    |                                                                                    |
| Must have a name                                                   | Anonymous                                                                          |
|                                                                    |                                                                                    |
| Arguments delimited by parentheses, separated  by commas           | Argument list terminated by a colon, separated by commas, and no parentheses       |
|                                                                    |                                                                                    |
| Support zero or more arguments zero arguments => empty parentheses | Support zero or more arguments zero arguments => lambda:                           |
|                                                                    |                                                                                    |
| Body is an indented block of statements                            | Body is a single expression                                                        |
|                                                                    |                                                                                    |
| A return statement is required to return anything other than None  | The return value is give by the body  expression. No return statement is permitted |
|                                                                    |                                                                                    |
| Can have docstrings                                                | Cannot have docstrings                                                             |
|                                                                    |                                                                                    |
| Easily tested as they can be fetched by name                       | Awkward or impossible to test                                                      |

* **calllable()** --> Returns Boolean value based on whether an object is a callable

* *args => positional arguments

* **kwargs => keyword arguments

* Order of arguments in a function are:
  1. Positional arguments (arg)
  2. *args
  3. Keyword arguments (kwarg) => When passed from calling a function should follow syntax name=value
  4. **kwargs 

