#!/usr/bin/env python3

# Theory of Computing project 2: NTM tracing program
#
# This project uses the prettytable library to print tables
# In order to install, please paste "python3 -m pip install -U prettytable"
# into the command line.
#
# This code traces the different paths a non-deterministic turing machine
# follows when evaluating a peice of input. The output includes the depth 
# of the configuration tree, the amound of transitions it takes, as well as
# the reult of the excecuting (either accept, reject, or halt due to excess depth).
# 
# The program takes in a csv file of a machine as outlined in the project description.
# The a_plus machine is taken directly from the project description pdf. Additionally,
# each NTM has an accompanying deterministic version to compare the steps and number of 
# transitions a DTM would take to perform the same task.
#
# To run the program, one should call the main function, the machine they want to run, 
# where they want to print output, and the maximum depth they want the machine to run.
# The call should look like this on the command line:
# Code/main_ncichosk.py Data/{desired NTM}.csv Output/{desired output file}.txt 50
# Users may print output to stdout by typing none as the output file and choose not to 
# include a maximum tree depth in which case the program would default to 50
#
# After a machine is called, the user will be prompted to enter strings for the machine 
# to run. In order to exit the program, enter the empty string.

import sys
import csv
from functions_ncichosk import run_machine
from prettytable import PrettyTable

def main():

    try: # Attempts to open the 
        with open(sys.argv[1], 'r') as file:
            reader = csv.reader(file)

            machine = next(reader)[0] # Reads in name of machine
            next(reader) # Skips over state names
            next(reader) # Skips over input characters
            next(reader) # Skips over tape characters
            start = next(reader)[0] # Reads in start state
            accept = next(reader)[0] # Reads in accept state
            reject = next(reader)[0] # Reads in reject state
            rules = []
            for line in reader: # Reads in the rules of the machine
                rules.append(line)

    except FileNotFoundError: # Prints an error if a valid file is not provided
        print(f'Error: File {sys.argv[1]} invalid \n')
        return -1

    output_file = sys.argv[2] 
    if output_file == 'none': # Sets up to write to output file
        outfile = None
    else:
        outfile = open(f'Output/output_{output_file}_ncichosk.txt', "w")
    try: # Sets maximum depth with a default of 100
        max_depth = int(sys.argv[3])
    except:
        max_depth = 100


    layer_total = 0
    transition_total = 0
    table = PrettyTable() # Initializes an output talbe using PrettyTable
    table.field_names = ["Machine", "Input String", "Result", "Depth", "Configurations Explored", "Average Nondeterminism", "Comments"]
    while True: # Reads in and runs input strings
        input_string = input("Enter a string: ")

        if not input_string:
            break

        comments = input("Enter comments: ")

        # Runs machine and saves output
        transitions, depth, solved, accepted, results = run_machine(input_string, rules, start, accept, reject, max_depth)
        layer_total += depth
        transition_total += transitions

        if solved == False:
            result = "Halted"
        else:
            if accepted == True:
                result = "Accepted"
            else:
                result = "Rejected"

        table.add_row([machine, input_string, result, depth, transitions, transitions/depth, comments])

        if outfile: # Writes to outfile if specified
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
            outfile.write(f'Average non-determinism: {transitions / depth}\n')
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
            print(f'Average non-determinism: {transitions / depth}')
            print(f'Configuration Tree:')
            for item in results:
                print(item)
            print()

    final_comments = input("Enter final comments: ")

    if outfile:
        outfile.write(f'Average determinism for inputted strings: {transition_total / layer_total}\n')
        outfile.write(f'This represents the average number of possible states at each step of the machine.\n')
        table.add_row([machine, "Totals", "N/A", layer_total, transition_total, transition_total/layer_total, final_comments])
        table_outfile = open(f'Tables/table_{output_file}_ncichosk.txt', "w")
        table_outfile.write(f'Table of tested strings for {machine}\n\n')
        table_outfile.write(f'{table}\n')

    else:
        print(f'Average determinism for inputted strings: {transition_total / layer_total}')
        print(f'This represents the average number of possible states at each step of the machine.')
        table.add_row([machine, "Totals", "N/A", layer_total, transition_total, transition_total/layer_total, final_comments])
        print(f'Table of tested strings for {machine}\n')
        print(table)

if __name__ == "__main__":
    if len(sys.argv) < 0: # Prints error if incorrect amount of input is used
        print("Usage: script.py <machine_csv_file> output_file [max_depth]")
        print("Program can print to stdout by typing none for the output_file")
    else:
        main()