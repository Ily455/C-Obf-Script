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

predefined_types = {
    'clock_t', 'size_t', 'ptrdiff_t', 'wchar_t', 'int8_t', 'uint8_t', 'int16_t',
    'uint16_t', 'int32_t', 'uint32_t', 'int64_t', 'uint64_t', 'intptr_t', 'uintptr_t',
    'intmax_t', 'uintmax_t', 'time_t', 'clockid_t', 'pid_t', 'gid_t', 'uid_t', 'mode_t',
    'dev_t', 'off_t', 'ino_t', 'blkcnt_t', 'blksize_t', 'fsblkcnt_t', 'fsfilcnt_t',
    'key_t', 'va_list'
}

excluded=keywords.union(preprocessors.union(backslashes.union(standard_functions.union(predefined_types))))

###INCLUDES###

# key = ''.join(random.choice(string.ascii_letters) for _ in range(64))

# print(f"here is the key, include it in the top of the obfuscated C code in order to print readable strings")

# key = "hh"

# encrypt_key=f'#define SECRET_KEY "{key}"'+'''\n'''

# encrypt=r'''#define ENCRYPT(text) ({ char *encrypted_text = (char *)malloc(strlen(text) + 1); for (size_t i = 0; i < strlen(text); i++) { encrypted_text[i] = text[i] ^ SECRET_KEY[i % strlen(SECRET_KEY)]; } encrypted_text[strlen(text)] = '\0'; encrypted_text; })'''+'''\n'''


###FUNCTIONS###

def remove_headers(code):
  pattern = r"""^\s*#(include|define|undef|if|ifdef|ifndef|else|elif|endif|line|error|pragma).*?$"""
  removed_lines, removed_header, removed_lib, removed_macro = [], [], [], []
  for match in re.finditer(pattern, code, flags=re.MULTILINE):
    removed_lines.append(match.group(0).strip("\n"))
    kind = match.group(1)
    if kind in ("include",):
      removed_lib.append(match.group(0).strip("\n"))
    elif kind in ("define", "ifdef", "ifndef"):
      removed_macro.append(match.group(0).strip("\n"))
    else:
      removed_header.append(match.group(0).strip("\n"))
  code = '\n'.join([line for line in code.splitlines() if line not in removed_lines])
#   print(code)

  return code, removed_header, removed_lib, removed_macro

def add_headers(code, removed_header):
    # def delete_empty_lines(text):
    #     lines = text.split('\n')
    #     non_empty_lines = [line for line in lines if line.strip()]
    #     result = '\n'.join(non_empty_lines)

    #     return result
    headers = '\n'.join(removed_header)
    # return delete_empty_lines(headers + '\n' + code)
    return headers + '\n' + code
def remove_comments(code):
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    code = re.sub(r'//.*?\n', '\n', code)
    return code

def remove_whitespace(code):
    code = re.sub(r'\s+', ' ', code)
    return code

# def encrypt_str(str):
#     encrypted_text = ""
#     for i in range(len(str)):
#         encrypted_text += chr((ord(str[i]) ^ ord(key[i % len(key)])))
#     print(encrypted_text.encode())
#     return encrypted_text.encode()

def replace_identifiers(code):

    def find_variables(code):
        pattern = r"(?:\w+\s+)(?!main)(?:\*)*([a-zA-Z_][a-zA-Z0-9_]*)"
        variable_declarations = re.findall(pattern, code)
        variables = set()
        for declaration in variable_declarations:
            if declaration not in excluded:
                tokens = declaration.strip().split()
                variables.add(tokens[0])
        return variables

    def rename_vars(code, variable_mapping):
        pattern = r'"(?:\\.|[^"\\])*?"'
        qsp_texts = re.findall(pattern, code)
        # mapped_encryptions={}
        # enc_qsp_texts=[]
        # for t in range(len(qsp_texts)):
        #     enc_qsp_texts.append(str(encrypt_str(qsp_texts[t]))[1:].replace("\\","\\\\"))
        #     mapped_encryptions[qsp_texts[t]] = enc_qsp_texts[t]
        # quotes={qt for qt in enc_qsp_texts}
        quotes={qt for qt in qsp_texts}
        mapped_quotes=map_vars(quotes)
        # print(mapped_encryptions)
        # print(mapped_quotes)
        #encrypt strs
        # for variable, replacement in mapped_encryptions.items():
        #     code = code.replace(r"{}".format(variable), replacement)
        # print(code)
        # replace encs with their corresponding randoms
        for variable, replacement in mapped_quotes.items():
            code = re.sub(r'{}'.format(re.escape(variable)), replacement, code)
        #randomizing identifiers
        for variable, replacement in variable_mapping.items():
            code = re.sub(r'\b{}\b'.format(re.escape(variable)), replacement, code)
        #bringing back the strs
        for variable, replacement in mapped_quotes.items():
            # code = code.replace(replacement, 'ENCRYPT('+variable+')')
            code = code.replace(replacement, variable)
            # print(variable)
        return code

    def map_vars(vars):
        variable_mapping = {}
        for variable in vars:
            random_string = ''.join(random.choice(string.ascii_letters) for _ in range(32))
            variable_mapping[variable] = random_string
        return variable_mapping

    codeVars=find_variables(code)
    # print(codeVars)
    map=map_vars(codeVars)
    newCode=rename_vars(code, map)
    return newCode

def preprocess_code(code):
    code = remove_comments(code)
    code, removed_header, removed_lib, removed_macros = remove_headers(code)
    code = remove_whitespace(code)
    code = add_headers(code, removed_macros)
    code = replace_identifiers(code)
    # code = add_headers(code, removed_header)
    code = add_headers(code, removed_lib)
    # print(removed_lib)
    # print(removed_header)
    # print(removed_macros)
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
###old impl###
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

##########################################################################################################

    # excluded_functions = ["printf", "puts", "fputs", "fprintf", "fputc", "fwrite", "putchar"]
    # def find_function_calls(code):
    #     # Regular expression pattern to find function calls with their arguments
    #     pattern = r'\b(?:printf|puts|fputs|fprintf|fputc|fwrite|putchar)\s*\((?:[^()]|\((?:[^()]+|\([^()]*\))*\))*\);'
    #     return re.findall(pattern, code)

    # def replace_identifiers_within_functions(text, excluded_functions, variable_mapping, detected_identifiers):
    #     for function_call in excluded_functions:
    #         # Exclude function calls that are in the excluded list
    #         if any(func in function_call for func in excluded_functions):
    #             continue
    #         # Replace identifiers within the function call
    #         for variable, replacement in variable_mapping.items():
    #             if variable in detected_identifiers:
    #                 # If the identifier was already detected, replace it with the same new string
    #                 text = text.replace(variable, replacement)
    #     return text