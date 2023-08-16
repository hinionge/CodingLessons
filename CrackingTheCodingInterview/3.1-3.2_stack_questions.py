# 16.8.2023
# CTCI Chapter 3 Q3.1

####### QUESTION: Describe how you would use a single array to implement three stacks.

                            # I would store the first stack in cells of index 3n
                            # the second stack in cells of index 3n+1
                            # and the third stack in cells of index 3n+2


# CTCI Chapter 3 Q3.2

####### QUESTION: How would you design a stack which, in addition to push and pop, has a function min() which returns
#######           the minimum element? Push, pop and min should all operate in O(1) time.

                            # At the start of the algorithm I would open an array of items which store two variables:
                            # min, and, atsize
                            # Every time an element is pushed, it is compared to min. If it is larger, do nothing.
                            # If it is smaller, add to the array the new min, together with atsize: the size of the stack.
                            # When an item is popped from the stack, the array of min/atsize updates to reflect.
                            # When the min function is called, it looks at the current size of the stack
                            # -- if the stack is the same size, then the latest min + atsize will be correct.
                            # If there have been repetaed pops, the array will still hold the correct information about
                            # the state of the stack in the past, and return that.
                            