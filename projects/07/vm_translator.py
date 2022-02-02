############################################################################################################################################################################

# Chapter 7 - VM Translator (stack arithmetic, memory access)

from typing import Optional

############################################################################################################################################################################

label_counter: int = 0

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

def clean_whitespace(lines: list[str]) -> list[str]:

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

def pop_from_stack(write_to_d: bool) -> list[str]:

    lines = ['@SP', 'M=M-1', 'A=M']

    if write_to_d:
        lines.extend(['D=M'])

    return lines

def push_to_stack(input: Optional[str] = '', read_from_d: Optional[bool] = False) -> list[str]:
    '''
    Write input value to stack and increment stack pointer
    '''
    if read_from_d:
        return ['@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    else:
        return [f'@{input}', 'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']

def push_from_symbol(symbol: str, offset: str) -> list[str]:
    '''
    Push value at address / offset to stack
    RAM[1] = LCL (local)
    RAM[2] = ARG (argument)
    RAM[3] = THIS
    RAM[4] = THAT
    RAM[5-12] = TEMP
    '''
    lines = []
    lines.extend([f'// PUSH value from {symbol} to stack'])

    # get initial address
    if symbol == 'TEMP':
        lines.extend(['@5'])

    else:
        lines.extend([f'@{symbol}'])

    # read value from address + offset
    for i in range(int(offset)):
        lines.extend([f'M=M+1'])
    lines.extend(['M=D'])
    # write value to stack
    lines.extend(push_to_stack(read_from_d = True))

    return lines

def pop_to_symbol(symbol: str, offset: str) -> list[str]:
    '''
    Pop value from stack and write to address referenced by symbol / offset
    RAM[1] = LCL (local)
    RAM[2] = ARG (argument)
    RAM[3] = THIS
    RAM[4] = THAT
    RAM[5-12] = TEMP
    '''
    lines = []
    lines.extend([f'// POP value from stack to {symbol}'])

    # read value from stack -> save to RAM[13]
    lines.extend(pop_from_stack(write_to_d = True))

    # get initial address
    if symbol == 'TEMP':
        lines.extend(['@5'])

    else:
        lines.extend([f'@{symbol}'])
        lines.extend(['A=M'])

    # write value to address + offset # TODO -> check if this works with A?
    for i in range(int(offset)):
        lines.extend([f'M=M+1'])

    lines.extend(['M=D'])

    return lines

def increment_stack_pointer() -> list[str]:

    return ['@SP', 'M=M+1']

def math_operation(operator: str) -> list[str]:
    '''
    Perform math operation with 2 operands in asm
    operator can be +, -, |, &
    '''
    operator_map = {'add': '+', 'sub': '-', 'or': '|', 'and': '&'}
    lines = []
    lines.extend([f'// math operation with operator: {operator}'])

    # pop first operand (to register D)
    lines.extend(pop_from_stack(write_to_d = True))

    # pop second operand (to M)
    lines.extend(pop_from_stack(write_to_d = False))

    # perform operation
    lines.extend([f'M=M{operator_map[operator]}D'])

    lines.extend(increment_stack_pointer())

    return lines

def if_else_operation(if_condition, true_statement, false_statement) -> list[str]:
    '''
    Add if / else statement implemented through 2 labels
    '''
    global label_counter
    lines = []
    lines.extend(['// if / else'])

    # if condition is met -> jump to TRUE
    lines.extend([f'@IF_ELSE_{label_counter}.TRUE'])
    lines.extend(if_condition)

    # FALSE case -> jump to END
    lines.extend(false_statement)
    lines.extend([f'@IF_ELSE_{label_counter}.END', '0;JMP'])

    # TRUE case
    lines.extend([f'(IF_ELSE_{label_counter}.TRUE)'])
    lines.extend(true_statement)

    # END of if/else statement
    lines.extend([f'(IF_ELSE_{label_counter}.END)'])

    label_counter += 1

    return lines

def logic_operation(logic_command: str) -> list[str]:

    lines = []

    lines.extend([f'// logic operation: {logic_command}'])

    # pop first operand (to register D)
    lines.extend(pop_from_stack(write_to_d = True))

    ## 1 operand operation
    if logic_command == 'neg':
        lines.extend(['M=-D'])

    elif logic_command == 'not':
        lines.extend(['M=!D'])

    ##  2 operand comparison
    logic_map = {'eq': 'JEQ', 'lt': 'JLT', 'gt': 'JGT'}

    if logic_command in logic_map.keys():

        # pop second operand (to M)
        lines.extend(pop_from_stack(write_to_d = False))

        lines.extend(['MD=M-D'])

        # handle if / else
        lines.extend(if_else_operation(
            if_condition = [f'D;{logic_map[logic_command]}'],
            true_statement = ['@SP', 'A=M', 'M=-1'],
            false_statement = ['@SP', 'A=M', 'M=0']))

    lines.extend(increment_stack_pointer())

    return lines

def initialize_asm() -> list[str]:
    '''
    Initialize pointers
    '''
    lines = []
    lines.extend(['@256', 'D=A', '@SP', 'M=D'])

    return lines

def parse_multiple_lines(lines) -> list[str]:

    math_commands = ['add', 'sub', 'or', 'and']
    logic_commands = ['eq', 'lt', 'gt', 'neg', 'and', 'or', 'not']

    pointers = {'this': 'THIS', 'that': 'THAT', 'local': 'LCL', 'argument': 'ARG', 'temp': 'TEMP'}

    return_lines = []

    # initialize asm file
    return_lines.extend(initialize_asm())

    # translate line by line
    for line in lines:
        input = line.split(' ')

        # push from / to stack
        if input[0] == 'push':
            if input[1] == 'constant':
                return_lines.extend(push_to_stack(input = input[-1]))

            elif input[1] in pointers.keys():
                return_lines.extend(push_from_symbol(symbol = pointers[input[1]], offset = input[-1]))

        # pop from / to stack
        elif input[0] == 'pop':
            if input[1] in pointers.keys():
                return_lines.extend(pop_to_symbol(symbol = pointers[input[1]], offset = input[-1]))

        # math or logic operation
        elif input[0] in math_commands:
            return_lines.extend(math_operation(input[0]))

        elif input[0] in logic_commands:
            return_lines.extend(logic_operation(input[0]))

    # end with infinite loop (nand2tetris convention)
    return_lines.extend(['(INFINITE_LOOP)', '@INFINITE_LOOP', '0;JMP'])

    return return_lines

def translate(input_file: str) -> None:

    print(f'Translating file {input_file}...\n')

    lines = [line.strip() for line in read_input_as_str(input_file)]
    lines = clean_whitespace(lines)

    output = parse_multiple_lines(lines)

    print('Output: ', output)

    output_file = input_file.replace('.vm', '.asm')
    write_output_to_file(output, output_file)

############################################################################################################################################################################

if __name__ == "__main__":

    # Part 1
    # arithmetic_files = ['./StackArithmetic/SimpleAdd/SimpleAdd.vm', './StackArithmetic/StackTest/StackTest.vm']

    # for file in arithmetic_files:
    #     translate(file)

    # Part 2
    memory_files = ['./MemoryAccess/BasicTest/BasicTest.vm']

    for file in memory_files:
        translate(file)

############################################################################################################################################################################