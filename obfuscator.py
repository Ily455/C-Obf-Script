###SCRIPT WRITTEN BY @ILY455, REFER TO https://github.com/Ily455/C-Obf-Script FOR LICENSE AND USAGE
###THIS SCRIPT IS NOT TESTED FOR PRODUCTION ENVIRONMENTS, MAKE SURE YOU DO SO BEFORE RELYING ON ANY OF ITS OUTCOMES
###############################################################################
#### OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF-OBF###
###############################################################################
import re
import random
import string
import sys
import os

###EXCLUDES###
backslashes={"\n", "\t", "\0"}

keywords={"alignas", "alignof", "auto", "bool", "break", "case", "char", "const", "constexpr", "continue",
    "default", "do", "double", "else", "enum", "extern", "false", "float", "for", "goto", "if", "inline",
    "int", "long", "main", "nullptr", "register", "restrict", "return", "short", "signed", "sizeof", "static",
    "static_assert", "struct", "switch", "thread_local", "true", "typedef", "typeof", "typeof_unqual",
    "union", "unsigned", "void", "volatile",
    "_Alignas", "_Alignof", "_Atomic", "_BitInt", "_Bool", "_Complex", "_Decimal128", "_Decimal32",
    "_Decimal64", "_Generic", "_Imaginary", "_Noreturn", "_Static_assert", "_Thread_local"}

preprocessors = {
    "if", "elif", "else", "endif","ifdef", "ifndef", "elifdef", "elifndef", "define", "undef",
    "include", "embed", "line", "error", "warning", "pragma", "defined", "__has_include", 
    "__has_embed", "__has_c_attribute"}

standard_functions = {
    "abort", "abs", "acos", "asin", "atan", "atan2", "atexit", "atof", "atoi", "atol", "bsearch", 
    "calloc", "ceil", "clearerr", "clock", "cos", "cosh", "ctime", "difftime", "div", "exit", 
    "exp", "fabs", "fclose", "feof", "ferror", "fflush", "fgetc", "fgetpos", "fgets", "floor", 
    "fmod", "fopen", "fprintf", "fputc", "fputs", "fread", "free", "freopen", "frexp", "fscanf", 
    "fseek", "fsetpos", "ftell", "fwrite", "getc", "getchar", "getenv", "gets", "gmtime", 
    "isalnum", "isalpha", "iscntrl", "isdigit", "isgraph", "islower", "isprint", "ispunct", 
    "isspace", "isupper", "isxdigit", "labs", "ldexp", "ldiv", "localeconv", "localtime", "log", 
    "log10", "longjmp", "malloc", "mblen", "mbstowcs", "mbtowc", "memchr", "memcmp", "memcpy", 
    "memmove", "memset", "mktime", "modf", "perror", "pow", "printf", "putc", "putchar", 
    "puts", "qsort", "raise", "rand", "realloc", "remove", "rename", "rewind", "scanf", 
    "setbuf", "setjmp", "setlocale", "setvbuf", "signal", "sin", "sinh", "sprintf", "sqrt", 
    "srand", "sscanf", "strcat", "strchr", "strcmp", "strcoll", "strcpy", "strcspn", "strerror", 
    "strftime", "strlen", "strncat", "strncmp", "strncpy", "strpbrk", "strrchr", "strspn", 
    "strstr", "strtod", "strtok", "strtol", "strtoul", "strxfrm", "system", "tan", "tanh", 
    "time", "tmpfile", "tmpnam", "tolower", "toupper", "ungetc", "vfprintf", "vprintf", 
    "vsprintf"
}

excluded=keywords.union(preprocessors.union(backslashes.union(standard_functions)))

###FUNCTION###
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
    
    print(removed_header, removed_lib, removed_macros)
    return code, removed_header, removed_lib, removed_macros

def add_headers(code, removed_header):
    def delete_empty_lines(text):
        lines = text.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        result = '\n'.join(non_empty_lines)
        
        return result
    headers = '\n'.join(removed_header)
    return delete_empty_lines(headers + '\n' + code)


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
    excluded_functions = ["printf", "puts", "fputs", "fprintf"]
    def find_function_calls(code):
        # Regular expression pattern to find function calls with their arguments
        pattern = r'\b(?:printf|puts|fputs|fprintf|fputc|fwrite|putchar)\s*\((?:[^()]|\((?:[^()]+|\([^()]*\))*\))*\);'
        return re.findall(pattern, code)
    
    def replace_identifiers_within_functions(text, excluded_functions, variable_mapping, detected_identifiers):
        for function_call in find_function_calls(text):
            # Exclude function calls that are in the excluded list
            if any(func in function_call for func in excluded_functions):
                continue
            # Replace identifiers within the function call
            for variable, replacement in variable_mapping.items():
                if variable in detected_identifiers:
                    # If the identifier was already detected, replace it with the same new string
                    text = text.replace(variable, replacement)
        return text
        
    def find_variables(code):
        pattern = r'\b[A-Za-z_][A-Za-z0-9_]*\s*(?:\[\s*\d*\s*\])?\s*;'
        pattern = r"(?:\w+\s+)(?!main)(?:\*)*([a-zA-Z_][a-zA-Z0-9_]*)"
        variable_declarations = re.findall(pattern, code)
        variables = set()
        for declaration in variable_declarations:
            if declaration not in excluded:
                tokens = declaration.strip().split()
                variables.add(tokens[0])
        print(variables)
        return variables
    
    def rename_vars(code, variable_mapping):
        for variable, replacement in variable_mapping.items():
            code = re.sub(r'\b{}\b'.format(re.escape(variable)), replacement, code)
        return code
    
    def map_vars(vars):
        variable_mapping = {}
        for variable in vars:
            random_string = ''.join(random.choice(string.ascii_letters) for _ in range(32))
            variable_mapping[variable] = random_string
        return variable_mapping
    
    codeVars=find_variables(code)
    map=map_vars(codeVars)
    newCode=replace_identifiers_within_functions(code, excluded_functions, codeVars, map)
    newCode=rename_vars(newCode, map)
    return newCode

def preprocess_code(code):
    code = remove_comments(code)
    code, removed_header, removed_lib, removed_macros = remove_headers(code)
    code = remove_whitespace(code)
    code = add_headers(code, removed_macros)
    code = replace_identifiers(code)
    code = add_headers(code, removed_header)
    code = add_headers(code, removed_lib)
    # code = remove_whitespace(code)
    return code

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

    processed_code = preprocess_code(c_code)

    output_dir = os.path.dirname(input_file)
    
    output_file = os.path.join(output_dir, 'obfuscated_' + os.path.basename(input_file))
    
    with open(output_file, 'w') as file:
        file.write(processed_code)

    print(f"Obfuscated code written to '{output_file}'.")

##########################################################
# def replace_identifiers(code):
#     # Define sets for predefined keywords, constants, and types
#     predefined_keywords = {
#         'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double',
#         'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register',
#         'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef',
#         'union', 'unsigned', 'void', 'volatile', 'while', 'clock', 'printf', 'define', 'main', 'srand', 'time', 'rand', '\n'
#     }

#     predefined_constants = {
#         'NULL', 'true', 'false', 'CLOCKS_PER_SEC'
#     }

#     predefined_types = {
#         'clock_t', 'size_t', 'ptrdiff_t', 'wchar_t', 'int8_t', 'uint8_t', 'int16_t',
#         'uint16_t', 'int32_t', 'uint32_t', 'int64_t', 'uint64_t', 'intptr_t', 'uintptr_t',
#         'intmax_t', 'uintmax_t', 'time_t', 'clockid_t', 'pid_t', 'gid_t', 'uid_t', 'mode_t',
#         'dev_t', 'off_t', 'ino_t', 'blkcnt_t', 'blksize_t', 'fsblkcnt_t', 'fsfilcnt_t',
#         'key_t', 'va_list'
#     }

#     # Combine predefined keywords, constants, and types
#     exclude_identifiers = predefined_keywords.union(predefined_constants, predefined_types)
    
#     # Generate a mapping of identifiers to replacement strings
#     identifier_map = {}
#     for identifier in re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', code):
#         if identifier not in exclude_identifiers:
#             if identifier not in identifier_map:
#                 identifier_map[identifier] = ''.join(random.choice(string.ascii_letters) for _ in range(len(identifier)))
    
#     # Replace each user-defined identifier with the corresponding replacement string
#     for identifier, replacement in identifier_map.items():
#         code = re.sub(r'\b{}\b'.format(re.escape(identifier)), replacement, code)
    
#     # Exclude identifiers within printf function calls
#     def exclude_printf(match):
#         printf_string = match.group(0)
#         return printf_string.replace(match.group(1), ' ' * len(match.group(1)))

#     code = re.sub(r'printf\s*\("([^"]*)"\)', exclude_printf, code)
    
#     return code