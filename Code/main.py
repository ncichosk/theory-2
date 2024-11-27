#!/usr/bin/env python3

import sys
import csv
from functions import run_machine

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

    input_string = sys.argv[2]

    output_file = sys.argv[3]
    if output_file == 'none':
        outfile = None
    else:
        outfile = open(sys.argv[3], "w")
    try:
        max_depth = int(sys.argv[4])
    except:
        max_depth = 100

    solved, accepted, results = run_machine(input_string, rules, start, accept, reject, max_depth)

    if outfile:
        outfile.write(f'Machine being run: {machine}\n')
        outfile.write(f'Input string: \"{input_string}\"\n')
        outfile.write(f'Automatic stop at depth of {max_depth}\n\n')
        outfile.write(f'Machine terminated: {solved}\n')
        outfile.write(f'Machine accepted: {accepted}\n')
        outfile.write(f'NTM Tree:\n')
        for item in results:
            outfile.write(f'{item}\n')

    else:
        print(f'Machine being run: {machine}')
        print(f'Input string: \"{input_string}\"')
        print(f'Automatic stop at depth of {max_depth}\n')
        print(f'Machine terminated: {solved}')
        print(f'Machine accepted: {accepted}')
        print(f'NTM Tree:')
        for item in results:
            print(item)

if __name__ == "__main__":
    if len(sys.argv) < 0: # Prints error if incorrect amount of input is used
        print("Usage: script.py <machine_csv_file> input_string output_file [max_depth]")
        print("Program can print to stdout by typing none for the output_file")
    else:
        main()