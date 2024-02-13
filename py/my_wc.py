import argparse
import os

# Create the argument parser
parser = argparse.ArgumentParser(description='Count the number of bytes in a file')

# Add the file path argument
parser.add_argument('file', type=str, help='Path to the file')

parser.add_argument('-c', help='Count the number of bytes in the file', action='store_true')

parser.add_argument('-l', help='Count the number of lines in the file', action='store_true')

# Parse the arguments
args = parser.parse_args()

# Read the file and count the bytes
try:
    # stat way
    if args.c or (not args.l and not args.c):
        print(f"Number of bytes in the file: {args.file} ", os.stat(args.file).st_size)
    if args.l:
        # straightforward way
        with open(args.file, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            print(f"Number of lines in the file: {args.file} ", len(lines))
except FileNotFoundError:
    print("File not found:", args.file)
except IOError:
    print("Error reading file:", args.file)