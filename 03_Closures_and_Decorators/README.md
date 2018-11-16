# Summary

* **def** is executed at run-time

* **def** defines the function in a scope from which it's called

* functions defined inside other functions are called **local functions**

* A new local function is created each time a containing function is executed

* Local functions are no different from other local name-bindings and can be treated like any other object

* Local functions can access names and other scopes via the **LEGB** rule

* The enclosing scope for local functions includes the paramteres of its enclosing function

* Local functions can be useful for code organization

* Local functions are similar to lambdas but are more general and powerful

* Functions can return other functions, including local functions defined in their bodies

* Closures allow local functions to access objects from scopes which have terminated

* Closures ensure that objects from terminated scopes are not garbage collected

* Functions with closures have a special __closure__ attribute

* Local functions in closures are the keys in implementing function factories, which are functions that create other functions

* **LEGB** does not apply to new name bindings

* We can access outer variables in a local function with **global** and **nonlocal** keywords

* We get a **SyntaxError** if the name doesn't exist when using nonlocal keyword

* Function decorators are used to modify the behavior of existing functions without having to change them directly

* Decorators are callable objects which accept a single callable object as an argument and return a new callable object

* You use the @ symbol to apply a decorator to functions

* Decorators can enhance maintainability, readability, and scalability of the designs

* Decorators can be any kind of callable object (functions, class objects, class instance)

* The **__name__** and **__doc__** attributes of decorated functions are actually those of their replacement function which is not always what you want

* You can manually update the __name__ and __doc__ of the wrapper function. You can achieve the same by using the wrapper function `@functools.wraps`

* Multiple decorators can be applied to a function. When there are multiple decorators, they are applied in **reverse order**

* Decorators don't have to be specially designed to work with other decorators

* Decorators are a powerful tool, but make sure you don't overuse them or use them unnecessarily

* There are technically no decorators that take extra arguments
to paramterize decorators, you need a function that creates decorators

* Local functions can create closures over objects on any number of enclosing scopes