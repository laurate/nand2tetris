############################################################################################################################################################################

# Chapter 6 - Assembler

import difflib

from copy import copy

############################################################################################################################################################################

dest_symbol_map = {
    'null': '000',
    '0': '000',
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111',
}

comp_symbol_map = {
    '0': '101010',
    '1': '111111',
    '-1': '111010',
    'D': '001100',
    'A': '110000',
    'M': '110000',
    '!D': '001101',
    '!A': '110001',
    '!M': '110001',
    '-D': '001111',
    '-A': '110011',
    '-M': '110011',
    'D+1': '011111',
    'A+1': '110111',
    'M+1': '110111',
    'D-1': '001110',
    'A-1': '110010',
    'M-1': '110010',
    'D+A': '000010',
    'D+M': '000010',
    'D-A': '010011',
    'D-M': '010011',
    'A-D': '000111',
    'M-D': '000111',
    'D&A': '000000',
    'D&M': '000000',
    'D|A': '010101',
    'D|M': '010101',
}

jump_symbol_map = {
    'null': '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

a_0_list = ['0', '1', '-1', 'D', 'A', '!D', '!A', '-D', '-A', 'D+1', 'A+1', 'D-1', 'A-1', 'D+A', 'D-A', 'A-D', 'D&A', 'D|A']
a_1_list = ['M', '!M', '-M', 'M+1', 'M-1', 'D+M', 'D-M', 'M-D', 'D&M', 'D|M']

predefined_symbol_map = {
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4,
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6,
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R10': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,
    'SCREEN': 16384,
    'KBD': 24576,
}

############################################################################################################################################################################

def read_input_as_str(input_file: str) -> list[str]:

    with open(input_file, 'r') as f:
        lines = f.readlines()

    return lines

def write_output_to_file(output: list[str], output_file: str) -> None:

    output = '\n'.join(output)

    with open(output_file, 'w') as f:
        f.write(output)
        f.close()

def parse_c_instruction(line) -> str:
    '''
    Parse C Instruction of format dest=comp;jump
    '''
    a = '0'
    comp = '000000'
    jump = '000'
    dest = '000'

    comp_symbol = None
    jump_symbol = None
    dest_symbol = None

    # 1. Identify symbols
    if ';' in line and not '=' in line:
        copy_line = copy(line)
        split_line_1 = copy_line.split(';')
        comp_symbol = split_line_1[0]
        jump_symbol = split_line_1[1]

    elif '=' in line and not ';' in line:
        split_line_2 = line.split('=')
        dest_symbol = split_line_2[0]
        comp_symbol = split_line_2[1]

    elif ';' in line and '=' in line:
        split_line_3 = line.split('=')
        dest_symbol = split_line_3[0]
        split_line_4 = split_line_3.split(';')
        comp_symbol = split_line_4[0]
        jump_symbol = split_line_4[1]

    # 2. Identify Comp / Jump / Dest
    # Comp Symbol
    if comp_symbol in a_0_list:
        a = 0
    elif comp_symbol in a_1_list:
        a = 1

    comp = comp_symbol_map[comp_symbol]

    # Jump Symbol
    if jump_symbol:
        jump = jump_symbol_map[jump_symbol]

    # Dest Symbol
    if dest_symbol:
        dest = dest_symbol_map[dest_symbol]

    c_instruction = f'111{a}{comp}{dest}{jump}'

    return c_instruction

def get_symbol_address(symbol, symbol_map) -> int:

    # predefined symbols
    if symbol in predefined_symbol_map.keys():
        int_value = predefined_symbol_map[symbol]

    # label symbols and variable symbols
    elif symbol in symbol_map.keys():
        int_value = symbol_map[symbol]

    else:
        int_value = symbol_map['current_address']
        symbol_map[symbol] = int_value
        symbol_map['current_address'] += 1

    return int_value

def parse_single_line(line, symbol_map) -> str:

    parse = ''

    # A instruction
    if line.startswith('@'):
        try:
            int_value = int(line.replace('@', ''))
        except:
            int_value = get_symbol_address(line.replace('@', ''), symbol_map)

        value = '{0:015b}'.format(int_value)
        parse = f'0{value}'

    # C instruction
    else:
        parse = parse_c_instruction(line)

    return parse

def parse_label_symbols(lines) -> dict:

    symbol_map = {}

    symbol_count = 0

    for line in lines:
        if line.startswith('('):
            index = lines.index(line) - symbol_count
            symbol_count += 1
            symbol = line.replace('(', '').replace(')', '')
            symbol_map[symbol] = index

    return symbol_map

def parse_multiple_lines(lines, symbol_map) -> list[str]:

    return_lines = []

    for line in lines:

        if line.startswith('('):
            continue

        return_lines.append(parse_single_line(line, symbol_map))

    return return_lines

def clean_whitespace(lines) -> list[str]:

    return_lines = []

    for line in lines:

        # ignore whitespace and comments
        if line == '' or line.startswith('//'):
            continue

        # handle in-line comments
        elif '//' in line:
            line = line.split('//')[0]

        return_lines.append(line.strip())

    return return_lines

def assemble(input_file: str) -> None:

    print(f'\nAssembling file {input_file}...')

    lines = [line.strip() for line in read_input_as_str(input_file)]
    lines = clean_whitespace(lines)

    # Assemble!
    symbol_map = parse_label_symbols(lines)
    symbol_map['current_address'] = 16
    lines = parse_multiple_lines(lines, symbol_map)

    # Write assembled output to file
    solution_file = input_file.replace('.asm', '.hack')
    output_file = input_file.replace('.asm', '_.hack')
    write_output_to_file(lines, output_file)

    # Diff output and solution
    with open(output_file) as f1:
        output_text = [x.strip() for x in f1.readlines()]

    with open(solution_file) as f2:
        solution_text = [x.strip() for x in f2.readlines()]

    print('Comparing output...')
    issue_tracker = False
    for line in difflib.unified_diff(
        output_text,
        solution_text,
        fromfile = output_file,
        tofile = solution_file,
        lineterm='\n'):
        if '+' in line or '-' in line:
            issue_tracker = True
            print(f'Error in line: {line}')

    if not issue_tracker:
        print('Assembled successfully.')

############################################################################################################################################################################

if __name__ == "__main__":

    symbol_less_files = ['/add/Add.asm', '/max/MaxL.asm', '/pong/PongL.asm', '/rect/RectL.asm']

    for file in symbol_less_files:
        assemble(f'.{file}')

    symbol_files = ['/max/Max.asm', '/pong/Pong.asm', '/rect/Rect.asm']

    for file in symbol_files:
        assemble(f'.{file}')

############################################################################################################################################################################