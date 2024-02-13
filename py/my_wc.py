import argparse
import os

# Create the argument parser
parser = argparse.ArgumentParser(description='Count the number of bytes in a file')

# Add the file path argument
parser.add_argument('file', type=str, help='Path to the file')

parser.add_argument('-c', help='Count the number of bytes in the file', action='store_true')

parser.add_argument('-l', help='Count the number of lines in the file', action='store_true')

parser.add_argument('-w', help='Count the number of words in the file', action='store_true')

parser.add_argument('-m', help='Count the number of characters in the file', action='store_true')

# Parse the arguments
args = parser.parse_args()

# Read the file and count the bytes
try:
    # stat way
    if args.c or (not any([args.c, args.l, args.w, args.m])):
        print(f"Number of bytes in the file: {args.file} ", os.stat(args.file).st_size)
    if args.l:
        # straightforward way
        with open(args.file, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            print(f"Number of lines in the file: {args.file} ", len(lines))
    if args.w:
        # straightforward way
        with open(args.file, 'r', encoding="utf-8") as file:
            words = file.read().split()
            print(f"Number of words in the file: {args.file} ", len(words))
    if args.m:
        # straightforward way
        with open(args.file, 'r', encoding="utf-8") as file:
            characters = file.read()
            print(f"Number of characters in the file: {args.file} ", len(characters))
except FileNotFoundError:
    print("File not found:", args.file)
except IOError:
    print("Error reading file:", args.file)