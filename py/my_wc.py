import argparse
import os

# Create the argument parser
parser = argparse.ArgumentParser(description='Count the number of bytes in a file')

# Add the file path argument
parser.add_argument('file', type=str, help='Path to the file')

# Parse the arguments
args = parser.parse_args()

# Read the file and count the bytes
try:
    # stat way
    file_stats = os.stat(args.file)
    # straightforward way
    # with open(args.file, 'rb') as file:
    #     byte_count = len(file.read())
    #     print("Number of bytes in the file:", byte_count)
except FileNotFoundError:
    print("File not found:", args.file)
except IOError:
    print("Error reading file:", args.file)