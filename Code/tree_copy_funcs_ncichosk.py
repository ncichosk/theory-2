#!/usr/bin/env python3

# These functions are created to generate new copys of layers and tuples
# Setting a new_var = old_var in python points to the same data and does not 
# actually create a copy. These functions are used to alleviate that problem
# so new tuples and layers can be copied and edited without changing previous 
# layers/tuples.

def layer_copy(layer):
    new_layer = []
    for item in layer:
        new_layer.append(tuple_copy(item))
    return new_layer

def tuple_copy(tuple):
    new_tuple = []
    for item in tuple:
        new_tuple.append(str(item))
    return new_tuple