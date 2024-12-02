#!/usr/bin/env python3

import sys
import csv
from functions_ncichosk import run_machine

def main():

    try: 
        with open(sys.argv[1], 'r') as file:
            reader = csv.reader(file)

            machine = next(reader)[0]
            next(reader)
            next(reader)
            next(reader)
            start = next(reader)[0]
            accept = next(reader)[0]
            reject = next(reader)[0]
            rules = []
            for line in reader:
                rules.append(line)

    except FileNotFoundError: # Prints an error if a valid file is not provided
        print(f'Error: File {sys.argv[1]} invalid \n')
        return -1

    output_file = sys.argv[2]
    if output_file == 'none':
        outfile = None
    else:
        outfile = open(sys.argv[2], "w")
    try:
        max_depth = int(sys.argv[3])
    except:
        max_depth = 100

    while True:
        input_string = input("Enter a string: ")

        if not input_string:
            break

        transitions, depth, solved, accepted, results = run_machine(input_string, rules, start, accept, reject, max_depth)

        if outfile:
            outfile.write(f'Machine being run: {machine}\n')
            outfile.write(f'Input string: \"{input_string}\"\n')
            outfile.write(f'Automatic stop at depth of {max_depth}\n\n')
            outfile.write(f'Depth of configuration tree: {depth}\n')
            outfile.write(f'Total number of transitions: {transitions}\n')
            if solved == False:
                outfile.write(f'Excecution halted after {depth} layers\n')
            else:
                if accepted == True:
                    outfile.write(f'String accepted after {depth} transitions\n')
                else:
                    outfile.write(f'String rejected after {depth} transitions\n')
            outfile.write(f'Configuration Tree:\n')
            for item in results:
                outfile.write(f'{item}\n')
            outfile.write(f'\n')

        else:
            print(f'Machine being run: {machine}')
            print(f'Input string: \"{input_string}\"')
            print(f'Automatic stop at depth of {max_depth}\n')
            print(f'Depth of configuration tree: {depth}')
            print(f'Total number of transitions: {transitions}')
            if solved == False:
                print(f'Excecution halted after {depth} layers')
            else:
                if accepted == True:
                    print(f'String accepted after {depth} transitions')
                else:
                    print(f'String rejected after {depth} transitions')
            print(f'Configuration Tree:')
            for item in results:
                print(item)
            print()

if __name__ == "__main__":
    if len(sys.argv) < 0: # Prints error if incorrect amount of input is used
        print("Usage: script.py <machine_csv_file> output_file [max_depth]")
        print("Program can print to stdout by typing none for the output_file")
    else:
        main()