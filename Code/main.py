#!/usr/bin/env python3

import sys
import csv

def run_machine(input, rules, max_depth):
    pass

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
    max_depth = sys.argv[3]

    print(f'Rules for {machine}:\n')
    print(rules)


if __name__ == "__main__":
    if len(sys.argv) < 0: # Prints error if incorrect amount of input is used
        print("Usage: script.py <machine_csv_file> input_string max_depth")
    else:
        main()