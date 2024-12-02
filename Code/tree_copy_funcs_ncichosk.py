#!/usr/bin/env python3

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