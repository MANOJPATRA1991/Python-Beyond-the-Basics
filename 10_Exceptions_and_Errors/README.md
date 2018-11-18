# Summary

* Always specify an exception type while handling errors

* Exceptions are arranged in an inheritance hierarchy.

* When we specify an exception statement, any class which is a subclass of the specified class will be caught in addition to the specified class itself.

## Python2.7

BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
    +-- StopIteration
    +-- StandardError
    |    +-- BufferError
    |    +-- ArithmeticError
    |    |    +-- FloatingPointError
    |    |    +-- OverflowError
    |    |    +-- ZeroDivisionError
    |    +-- AssertionError
    |    +-- AttributeError
    |    +-- EnvironmentError
    |    |    +-- IOError
    |    |    +-- OSError
    |    |         +-- WindowsError (Windows)
    |    |         +-- VMSError (VMS)
    |    +-- EOFError
    |    +-- ImportError
    |    +-- LookupError
    |    |    +-- IndexError
    |    |    +-- KeyError
    |    +-- MemoryError
    |    +-- NameError
    |    |    +-- UnboundLocalError
    |    +-- ReferenceError
    |    +-- RuntimeError
    |    |    +-- NotImplementedError
    |    +-- SyntaxError
    |    |    +-- IndentationError
    |    |         +-- TabError
    |    +-- SystemError
    |    +-- TypeError
    |    +-- ValueError
    |         +-- UnicodeError
    |              +-- UnicodeDecodeError
    |              +-- UnicodeEncodeError
    |              +-- UnicodeTranslateError
    +-- Warning
         +-- DeprecationWarning
         +-- PendingDeprecationWarning
         +-- RuntimeWarning
         +-- SyntaxWarning
         +-- UserWarning
         +-- FutureWarning
         +-- ImportWarning
         +-- UnicodeWarning
         +-- BytesWarning

## Python3+

BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
    +-- StopIteration
    +-- ArithmeticError
    |    +-- FloatingPointError
    |    +-- OverflowError
    |    +-- ZeroDivisionError
    +-- AssertionError
    +-- AttributeError
    +-- BufferError
    +-- EOFError
    +-- ImportError
    +-- LookupError
    |    +-- IndexError
    |    +-- KeyError
    +-- MemoryError
    +-- NameError
    |    +-- UnboundLocalError
    +-- OSError
    |    +-- BlockingIOError
    |    +-- ChildProcessError
    |    +-- ConnectionError
    |    |    +-- BrokenPipeError
    |    |    +-- ConnectionAbortedError
    |    |    +-- ConnectionRefusedError
    |    |    +-- ConnectionResetError
    |    +-- FileExistsError
    |    +-- FileNotFoundError
    |    +-- InterruptedError
    |    +-- IsADirectoryError
    |    +-- NotADirectoryError
    |    +-- PermissionError
    |    +-- ProcessLookupError
    |    +-- TimeoutError
    +-- ReferenceError
    +-- RuntimeError
    |    +-- NotImplementedError
    +-- SyntaxError
    |    +-- IndentationError
    |         +-- TabError
    +-- SystemError
    +-- TypeError
    +-- ValueError
    |    +-- UnicodeError
    |         +-- UnicodeDecodeError
    |         +-- UnicodeEncodeError
    |         +-- UnicodeTranslateError
    +-- Warning
         +-- DeprecationWarning
         +-- PendingDeprecationWarning
         +-- RuntimeWarning
         +-- SyntaxWarning
         +-- UserWarning
         +-- FutureWarning
         +-- ImportWarning
         +-- UnicodeWarning
         +-- BytesWarning
         +-- ResourceWarning

* Since subclasses are programming errors, never catch **BaseException** or **Exception**

* **Only a single string argument should be used when raising an error.** We can get the error message by using `e.args` or by using `str(e)`

* **Exception Chaining** allows us to associate one exception with another, and there are two main use cases:
    1. **IMPLICIT CHAINING**: During processing of one exception another exception occurs
    2. **EXPLICIT CHAINING**: When we wish to deliberately handle an exception by translating it into a different exception type

* In Python 3+, each exception has a `__traceback__` attribute which contains a reference to the traceback object associated with the exception.

* **IMPORTANT**
    *Don't keep references of the traceback beyond the scope of the except block* as it contains reference to all the stack frame objects which comprises of call stacks and each stack frame contains references to all of its local variables. Maintaining references to these mean they won't be garbage collected.

* **ASSERTIONS**
    *syntax*:
        `assert condition [, message]` --> condition is a boolean expression and message is an optional string for an error

     If the condition is False an **AssertionError** exception is raised and if a message is supplied, it is used as the exception payload.

    Assertion should only be used to check the correctness of the function implementation *not the function arguments*.