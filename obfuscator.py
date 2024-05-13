import sys
import os
from utils import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python obfuscator.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            c_code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    output_dir = os.path.dirname(input_file)

    output_file = os.path.join(output_dir, 'obfuscated_' + os.path.basename(input_file))

    processed_code = preprocess_code(c_code, output_dir)

    with open(output_file, 'w') as file:
        file.write(processed_code)

    print(f"Obfuscated code written to '{output_file}'.")
