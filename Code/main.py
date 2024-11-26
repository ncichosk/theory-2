#!/usr/bin/env python3

import sys
import csv

def run_machine(input, rules, start, accept, reject, max_depth):
    depth = 0
    tree = []
    accept_flag = 0

    tree.append([["", start, input]])    

    while True:
        if accept_flag == 1:
            return True, True, tree
        if depth >= max_depth:
            return False, False, tree
        depth += 1
        
        old_layer = tree[-1]
        new_layer = []
        reject_states = []

        for config in old_layer:

            if config[1] == reject:
                reject_states.append(config)
            else:
                new_configs = update(config, rules)


            for item in new_configs:
                if item[1] == accept:
                    accept_flag = 1
                new_layer.append(item)

        for item in reject_states:
            new_layer.append(item)

        tree.append(new_layer)

def update(config, rules):
    tape_head = config[2][0]
    state = config[1]
    updates = []
    new_configs = []

    for rule in rules:
        if state == rule[0] and tape_head == rule[1]:
            updates.append(rule)

    for item in updates:
        temp = config
        

def main():

    try: 
        with open(sys.argv[1], 'r') as file:
            reader = csv.reader(file)

            machine = next(reader)[0]
            states = next(reader)
            epsilon = next(reader)
            gamma = next(reader)
            start = next(reader)[0]
            accept = next(reader)[0]
            reject = next(reader)[0]
            rules = []
            for line in reader:
                rules.append(line)

    except FileNotFoundError: # Prints an error if a valid file is not provided
        print(f'Error: File {sys.argv[1]} invalid \n')
        return -1

    input_string = sys.argv[2]

    output_file = sys.argv[3]
    if output_file == 'stdout':
        outfile = open(sys.stdout, "w")
    else:
        outfile = open(sys.argv[3], "w")
    try:
        max_depth = int(sys.argv[4])
    except:
        max_depth = None

    outfile.write(f'Machine being run: {machine}\n')
    outfile.write(f'Input string: \"{input_string}\"\n')
    outfile.write(f'Automatic stop at depth of {max_depth}\n\n')

    solved, accepted, results = run_machine(input_string, rules, start, accept, reject, max_depth)

    print(solved)
    print(accepted)
    for item in results:
        print(item)

if __name__ == "__main__":
    if len(sys.argv) < 0: # Prints error if incorrect amount of input is used
        print("Usage: script.py <machine_csv_file> input_string output_file [max_depth]")
    else:
        main()