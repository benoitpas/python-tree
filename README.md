python-tree
-----------
A simple program to help me prepare a project structure to use python for the advent of code 2021.

The implemenation is very similar to the [clojure](https://github.com/benoitpas/clojure-tree) one where I used a list to store the tree.

The twist in python is that I use a  python tuple instead of a list. List and tuples are very similar in python, the main difference is that tuple are immutable. 

As python is not typed, list can contains values of different types while in strongly typed languages like Haskell, Scala or even C++ list, all elements in a list have the same type.

A few interesting facts:
* `(1)` is not a tuple, it is just `1`. `(1,)` is a tuple containing only one value
* most list operations (like `reduce` in that example) work on tuples !