"""
How to Use the Script:
1. Save the above Python code to a file, for example, create_structure_from_tree.py.
2. Create your tree structure file (structure.txt) with the desired directory and file paths.
3. Run the script using Python:
    python create_structure_from_tree.py
4. Input the path to the structure file when prompted.

This script reads the tree-like directory structure from the file and directly creates the corresponding directories and files in the filesystem.
"""

import os
import re

def create_structure_from_tree(structure_file):
    with open(structure_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        # Remove leading spaces and tree symbols
        clean_line = re.sub(r'^[\s│├─]*', '', line).strip()

        # Determine if it's a directory or file
        if clean_line.endswith('/'):
            # If it's a directory and doesn't exist, create it
            if not os.path.exists(clean_line):
                os.makedirs(clean_line)
                print(f"Created directory: {clean_line}")
        else:
            # If it's a file, ensure its directory exists, then create the file
            dir_name = os.path.dirname(clean_line)
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name)
                print(f"Created directory: {dir_name}")
            with open(clean_line, 'w') as f:
                pass
            print(f"Created file: {clean_line}")

if __name__ == "__main__":
    structure_file = input("Enter the path to the structure file: ")
    create_structure_from_tree(structure_file)
