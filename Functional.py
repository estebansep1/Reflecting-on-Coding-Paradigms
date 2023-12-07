def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

arr =[[3, 1, 4], [1, 5, 9], [2, 6, 5, 3, 5]]
print(flatten_and_sort(arr))



# Thought Prompts

# How does this solution ensure data immutability?

"""
This solution ensures data immutability by not modifying the input array in place. It creates a new list with the flattened and sorted elements.
"""


# Is this solution a pure function? Why or why not?

"""
This is a pure function because it depends only on its input parameters and produces a result without any side effects.
"""

# Is this solution a higher order function? Why or why not?

"""
This solution is not a higher-order function because it does not take another function as an argument or return a function.
"""

# Would it have been easier to solve this problem using a different programming style?

"""
This solution seemed smooth to me just because i prefer writing functions instead of classes.
"""

# Why in particular is functional programming a helpful paradigm when solving this problem?

"""
Functional programming promotes immutability and pure function.
"""