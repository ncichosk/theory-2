#!/usr/bin/env python3

# This file contains the functions used in main.
# run_machine is called by main and calls all of the 
# subsequent functions.

from tree_copy_funcs_ncichosk import layer_copy, tuple_copy

def run_machine(input, rules, start, accept, reject, max_depth): # Main function for 
    depth = 0
    tree = []
    accept_flag = 0
    transitions = 0

    tree.append([["", start, input]]) # Initializes the start state to the tree

    while True:
        if accept_flag == 1: # Breaks loop if an accept state is found
            return transitions, depth, True, True, tree
        if depth >= max_depth: # Breaks loop if maximum depth is hit
            return transitions, depth, False, False, tree
        
        old_layer = layer_copy(tree[-1])
        new_layer = []

        for config in old_layer: # Updates each state in the layer
            if config[1] == reject: # Drops rejected states
                continue
            new_configs = update(config, rules, reject) # Finds new states

            for item in new_configs: # Appends new states to the new layer list
                if item[1] == accept:
                    accept_flag = 1
                new_layer.append(item)
                transitions += 1

        if new_layer == []: # Returns if all branches in previous layer were reject states
            return transitions, depth, True, False, tree

        tree.append(new_layer)
        depth += 1

def update(config, rules, reject): # Finds new states from a given input state
    tape_head = config[2][0]
    state = config[1]
    updates = []
    new_configs = []

    for rule in rules: # Adds relevant transitions to an update list
        if state == rule[0] and tape_head == rule[1]:
            updates.append(rule)

    for item in updates: # Appends each updated state to a list
        new_configs.append(update_config(tuple_copy(config), item))

    if new_configs == []: # If no rules are found, the new configuration goes to the reject state
        temp = config
        temp[1] = reject
        new_configs.append(temp)
        return new_configs

    return new_configs
         
def update_config(config, rule): # Updates a configuration for a given rule
        config = tuple_copy(config)
        before = list(config[0])
        after = list(config[2])

        after[0] = rule[3]
        config[1] = rule[2]

        if rule[4] == "R": # Moves the tape right
            hold = after.pop(0)
            before.append(hold)

            if after == []:
                after.append("_")

        if rule[4] == "L" and before != []: # Moves the tape left if there is room
            hold = before.pop()
            after.insert(0, hold)

        config[0] = "".join(before)
        config[2] = "".join(after)
        return config