# Fondeadora Coding Challenge - Mariana De la Vega

### Solution

The task was to flatten an array or arrays of integers (that can be nested). My solution works recursively by traversing the input array, item per item, until reaching the last one. Whenever an item is reached, the program checks if the item is an integer, a list or an invalid input. Depending on the type of the item: the number might be added to the output array, the array continues to be checked or an exception is raised.

The solution to this problem is not the most efficient. For time complexity, the worst case scenario (and the important one to consider) is O(2<sup>n</sup>) because every item we have 2 options: append to output array and continue with next number or traverse the nested array. For space complexity, it would be O(h) where h is the maximum height of the stack (depending on how deep the recursive calls went). 

### How to run?

* Run the main.py file to see the algorithm in action
* To test, use the shell terminal in repl.it and run `pytest`.
