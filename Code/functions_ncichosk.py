#!/usr/bin/env python3

from tree_copy_funcs_ncichosk import layer_copy, tuple_copy

def run_machine(input, rules, start, accept, reject, max_depth):
    depth = 0
    tree = []
    accept_flag = 0
    transitions = 0

    tree.append([["", start, input]])    

    while True:
        if accept_flag == 1:
            return transitions, depth, True, True, tree
        if depth >= max_depth:
            return transitions, depth, False, False, tree
        
        old_layer = layer_copy(tree[-1])
        new_layer = []

        for config in old_layer:
            if config[1] == reject:
                continue
            new_configs = update(config, rules, reject)

            for item in new_configs:
                if item[1] == accept:
                    accept_flag = 1
                new_layer.append(item)
                transitions += 1

        if new_layer == []:
            return transitions, depth, True, False, tree

        tree.append(new_layer)
        depth += 1

def update(config, rules, reject):
    tape_head = config[2][0]
    state = config[1]
    updates = []
    new_configs = []

    for rule in rules:
        if state == rule[0] and tape_head == rule[1]:
            updates.append(rule)

    for item in updates:
        new_configs.append(update_config(tuple_copy(config), item))

    if new_configs == []:
        temp = config
        temp[1] = reject
        new_configs.append(temp)
        return new_configs

    return new_configs
         
def update_config(config, rule):
        config = tuple_copy(config)
        before = list(config[0])
        after = list(config[2])

        after[0] = rule[3]
        config[1] = rule[2]

        if rule[4] == "R":
            hold = after.pop(0)
            before.append(hold)

            if after == []:
                after.append("_")

        if rule[4] == "L" and before != []:
            hold = before.pop()
            after.insert(0, hold)

        config[0] = "".join(before)
        config[2] = "".join(after)
        return config

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