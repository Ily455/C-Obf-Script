import re
import random
import string
import sys

def remove_headers(code):
    removed_header = []
    removed_lib = []
    removed_macros = []
    # Regular expression pattern to match header elements
    lib_pattern = r'^\s*#(include).*?$'
    macros_pattern = r'^\s*#(define|ifdef|ifndef).*?$'
    header_pattern = r'^\s*#(include|define|undef|if|ifdef|ifndef|else|elif|endif|line|error|pragma).*?$'
    # Find and remove headers, storing them in removed_header list
    code = re.sub(lib_pattern, lambda match: removed_lib.append(match.group(0)), code, flags=re.MULTILINE)
    code = re.sub(macros_pattern, lambda match: removed_macros.append(match.group(0)), code, flags=re.MULTILINE)
    code = re.sub(header_pattern, lambda match: removed_header.append(match.group(0)), code, flags=re.MULTILINE)
    return code, removed_header, removed_lib, removed_macros

def add_headers(code, removed_header):
    # Add removed headers back to the beginning of the code
    headers = '\n'.join(removed_header)
    return headers + '\n' + code


def remove_comments(code):
    # Remove C-style comments (/* ... */)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # Remove C++ style comments (// ...)
    code = re.sub(r'//.*?\n', '\n', code)
    return code

def remove_whitespace(code):
    # Remove extra whitespace
    code = re.sub(r'\s+', ' ', code)
    return code

def replace_identifiers(code):
    # Define sets for predefined keywords, constants, and types
    predefined_keywords = {
        'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double',
        'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register',
        'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef',
        'union', 'unsigned', 'void', 'volatile', 'while', 'clock', 'printf', 'define', 'main', 'srand', 'time', 'rand', '\n'
    }

    predefined_constants = {
        'NULL', 'true', 'false', 'CLOCKS_PER_SEC'
    }

    predefined_types = {
        'clock_t', 'size_t', 'ptrdiff_t', 'wchar_t', 'int8_t', 'uint8_t', 'int16_t',
        'uint16_t', 'int32_t', 'uint32_t', 'int64_t', 'uint64_t', 'intptr_t', 'uintptr_t',
        'intmax_t', 'uintmax_t', 'time_t', 'clockid_t', 'pid_t', 'gid_t', 'uid_t', 'mode_t',
        'dev_t', 'off_t', 'ino_t', 'blkcnt_t', 'blksize_t', 'fsblkcnt_t', 'fsfilcnt_t',
        'key_t', 'va_list'
    }

    # Combine predefined keywords, constants, and types
    exclude_identifiers = predefined_keywords.union(predefined_constants, predefined_types)
    
    # Generate a mapping of identifiers to replacement strings
    identifier_map = {}
    for identifier in re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', code):
        if identifier not in exclude_identifiers:
            if identifier not in identifier_map:
                identifier_map[identifier] = ''.join(random.choice(string.ascii_letters) for _ in range(len(identifier)))
    
    # Replace each user-defined identifier with the corresponding replacement string
    for identifier, replacement in identifier_map.items():
        code = re.sub(r'\b{}\b'.format(re.escape(identifier)), replacement, code)
    
    # Exclude identifiers within printf function calls
    def exclude_printf(match):
        printf_string = match.group(0)
        return printf_string.replace(match.group(1), ' ' * len(match.group(1)))

    code = re.sub(r'printf\s*\("([^"]*)"\)', exclude_printf, code)
    
    return code




def preprocess_code(code):
    code = remove_comments(code)
    code, removed_header, removed_lib, removed_macros = remove_headers(code)
    code = remove_whitespace(code)
    code = add_headers(code, removed_macros)
    code = replace_identifiers(code)
    code = add_headers(code, removed_header)
    code = add_headers(code, removed_lib)
    return code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python SICobfuscator.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            c_code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    processed_code = preprocess_code(c_code)

    output_file = "obfuscatedinput.c"
    with open(output_file, 'w') as file:
        file.write(processed_code)

    print(f"Obfuscated code written to '{output_file}'.")
