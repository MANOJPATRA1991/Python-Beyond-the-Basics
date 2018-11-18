# Summary

| PROTOCOLS\COLLECTIONS | str     | list    | range   | tuple   | set     | bytes   | dict    |
|-----------------------|---------|---------|---------|---------|---------|---------|---------|
| Container             | Y       | Y       | Y       | Y       | Y       | Y       | Y       |
| Sized                 | Y       | Y       | Y       | Y       | Y       | Y       | Y       |
| Iterable              | Y       | Y       | Y       | Y       | Y       | Y       | Y       |
| Sequence              | Y       | Y       | Y       | Y       |         | Y       |         |
| Set                   |         |         |         |         | Y       |         |         |
| Mutable Sequence      |         | Y       |         |         |         |         |         |
| Mutable Set           |         |         |         |         | Y       |         |         |
| Mutable Mapping       |         |         |         |         |         |         | Y       |

* Most collections implement container, sized and iterable.
* All except **dict** and **set** are sequences.

* *Container Protocol*
                -- Membership testing using `in` and `not in`
                -- Special method: `__contains__(item)`
                -- Fallback to iterable protocol

* *Sized Protocol*
                -- Determine number of elements with `len(s)`
                -- Must not consume or modify collection
                -- Special method: `__len__()`

* *Iterable Protocol*
                -- Can produce an iterator with `iter(s)`
                Special method: __iter__()
                ```
                for item in iterable:
                  do_something(item)
                ```
* *Sequence Protocol*
                -- Implies container, sized and iterable
                ```
                # Retrieve elements by index
                item = seq[index]

                # Find items by value
                index = seq.index(item)

                # Count items
                num = seq.count(item)

                # Produce a reversed sequences
                # Special method -- `__reversed__()`
                # Fallback to `__getitem__()` and `__len__()`
                r = reversed(seq)

                # Retrieve items by slicing
                item = seq[start:stop]
                ```
                --- Support concatenation with + operator
                    --- Special method: __add__()
                --- Support repetition with * operator
                    -- Special methods: __mul__() and __rmul__()

* *Set Protocol* --
              - Set algebra operations(methods and infix operators)
              -- subset `__le__()`, `<=`, `issubset()`          |
          -- proper subset, `__lt__()`, `<`                     |  \
              -- equal `__eq__()`, `==`                         |---\ Relational
              -- not equal `__ne__()`, `!=`                     |---/ Operators
              -- proper superset `__gt__()`, `>`                |  /
              -- superset `__ge__()`, `>=`, `issuperset()`      |
              -- disjoint `isdisjoint()`                        |
              -- intersections `__and__()`, `&`, `intersection()`               |  \
              -- union `__or__()`, `|`, `union()`                               |---\ Algebraic
              -- symmetric difference `__xor__()`, `^`, `symmetric_difference`  |---/ Operators
              -- difference `__sub__()`, `-`, `difference`                      |  /

* The differnce between the operand version and method version above is that operand versions require operands to be of the same type while methods take any iterable series as arguments

* It is not required but only encouraged to inherit from the appropriate abc's when implementing collections