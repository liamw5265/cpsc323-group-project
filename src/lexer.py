import sys
from pathlib import Path

identifier_transition_function = {
    'l': {'1': '2', '2': '3', '3': '3', '4': '3', '5': '3', '6': '6'},
    'd': {'1': '6', '2': '4', '3': '4', '4': '4', '5': '4', '6': '6'},
    '_': {'1': '6', '2': '5', '3': '5', '4': '5', '5': '5', '6': '6'}
}
identifier_accepting_states = ['2', '3', '4', '5']

integer_transition_function = {
    'd': {'1': '2', '2': '2'}
}

integer_accepting_states = ['2']

real_transition_function = {
    'd': {'1': '2', '2': '2', '3': '4', '4': '4', '5': '5'},
    '.': {'1': '3', '2': '3', '3': '5', '4': '5', '5': '5'}
}

real_accepting_states = ['4']

starting_state = '1'

operator_list = ['+', '-', '*', '/', '<', '>', '<=', '>=', '=', '==', '!=']

keywords_list = ['integer', 'boolean', 'real', 'if', 'else', 'fi', 'while', 
                 'return', 'get', 'put', 'true', 'false', 'function']

separator_list = ['(', ')', '{', '}', ' ', '@', ';', ',', ':', '\n', "'", '"']

comment = '!'

def convert_input_to_fsm_input(input_str: str) -> str:
    '''
    Turns input into input that the identifier_fsm can accept

    arguments:
        - input_str: 

    return (str): New form of input that the identifier_fsm can read
    '''

    result = ''

    if input_str in keywords_list:
        return -1

    for char in input_str:
        if char.isalpha():
            result += 'l'
        elif char.isdigit():
            result += 'd'
        elif char == '_':
            result += '_'
        elif char == '.':
            result += '.'
        else:
            result = -1
            break

    return result

def fsm(input_str: str,
        starting_states: str,
        accepting_states: list[str],
        transition_function: dict[str, dict[str, str]]
        ) -> bool:
    '''
    Checks [input_str] if it is a valid token

    arguments:
        - input_str: Proprosessed string variable
        - starting_stats: string variable for starting state
        - accepting_states: list of accepted states for related fsm
        - transition_function: nested dict for transition fucntion for 
                               related fsm

    returns (bool): True or False if [input_str] is a valid token relative to 
                    the transition functions passed
    '''

    new_input_str = convert_input_to_fsm_input(input_str)

    current_state = starting_states

    for input in str(new_input_str):
        try:
            next_state = transition_function[input][current_state]
            current_state = next_state
        except KeyError:
            return False

    if current_state in accepting_states:
        return True
    else:
        return False

def read_file(file_path: str) -> str:
    '''
    Read txt file and assign the data to a string variable

    arguments:
        - file_path: File path of document as a string

    returns (str): String variable of the data from the text document 
    '''

    with open(file_path, 'r', encoding = 'utf-8') as file:
        file_contents = file.read()

    input_without_comments = remove_comments(file_contents)

    return input_without_comments


def remove_comments(text_input: str) -> str:
    '''
    Removes all comments from the input string

    arguments:
        - text_input: The data from the input document as type string

    returns (str): String variable of the data from the text document without 
                   any comments
    '''

    inside_comment = False
    input_without_comments = ''

    for index in range(len(text_input) - 1):
        current_char = text_input[index]
        next_char = text_input[index + 1]

        if ((current_char == comment) and 
            (not inside_comment) and 
            (next_char != '=')):
            inside_comment = True
        elif ((current_char == comment) and 
              (inside_comment) and 
              (next_char != '=')):
            inside_comment = False
        elif not inside_comment:
            input_without_comments += current_char

    return input_without_comments

def separate_tokens(input_str: str) -> list[str]:
    '''
    Truns string input into list of tokens

    Arg:
        - input_str: Data from input document of type string without any comments

    Returns: list of tokens of type string
    '''

    # Goes char by char and adds to a string(token)
    # if the current char or token is an separator or operator 
    # add to list(tokens)
    tokens = []
    token = ''

    for index in range(len(input_str)):
        current_char = input_str[index]

        if ((current_char in separator_list) or 
            (current_char in operator_list) or 
            (token in separator_list) or 
            (token in operator_list)):
            tokens.append(token)
            token = ''

        token += current_char

    # keeps the last token
    if token:
        tokens.append(token)

    

    # The loop before separated <= and >= operators
    # Loop goes through each item is list, 
    # checks if current token and next token is operator
    with_double_op_tokens_list = []
    is_double_op = False

    for index in range(len(tokens)):
        if is_double_op:
            is_double_op = False
            continue

        #fix added because When index is at the 
        # last position in tokens, tokens[index + 1] doesn't exist
        if (index + 1 < len(tokens) and
        tokens[index] in operator_list and
        tokens[index + 1] in operator_list):
            double_op = tokens[index] + tokens[index + 1]
            with_double_op_tokens_list.append(double_op)   
            is_double_op = True     
        else:
            with_double_op_tokens_list.append(tokens[index])

    # Loops removes all spaces and newline chars
    final_token_list = []
    for token in with_double_op_tokens_list:
        if token != ' ' and token != '\n':
            final_token_list.append(token)
    return final_token_list

def print_token_and_lexeme(lexeme_list: list[str], output_file):
    '''
    Prints all lexem and their token type

    arguments:
        - lexeme_list: List of all lexemes 
    '''

    output_file.write('Token         Lexeme\n')
    output_file.write('-------------------\n')
    
    for lexeme in lexeme_list:
        token = 'Unknown'

        if lexeme in operator_list:
            token = 'Operator  '
        elif lexeme in separator_list:
            token = 'Separator '
        elif lexeme in keywords_list:
            token = 'Keyword   '
        elif fsm(lexeme,
                 starting_state,
                 integer_accepting_states,
                 integer_transition_function):
            token = 'Integer   '
        elif fsm(lexeme,
                 starting_state,
                 real_accepting_states,
                 real_transition_function):
            token = 'Real      '
        elif fsm(lexeme,
                 starting_state,
                 identifier_accepting_states,
                 identifier_transition_function):
            token = 'Identifier'

        output_file.write(f'{token:<12} {lexeme}\n')

def lexer(input_file_path: str, output_file_path: str):
    '''
    '''
    no_comment_text = read_file(input_file_path)
    token_list = separate_tokens(no_comment_text)
    print_token_and_lexeme(token_list, output_file_path)
        

if __name__ == '__main__':
    # Find the project folder whether running Python or the .exe
    if getattr(sys, 'frozen', False):
        project_root = Path(sys.executable).resolve().parent.parent
    else:
        project_root = Path(__file__).resolve().parent.parent

    test_cases = [
        project_root / 'tests/lexer_test_cases/test_case_1.txt',
        project_root / 'tests/lexer_test_cases/test_case_2.txt',
        project_root / 'tests/lexer_test_cases/test_case_3.txt'
    ]

    output_folder = project_root / 'outputs'
    output_folder.mkdir(parents=True, exist_ok=True)

    for index, test_file in enumerate(test_cases, start=1):
        output_path = output_folder / f'output_{index}.txt'

        with open(output_path, 'w', encoding='utf-8') as output_file:
            lexer(test_file, output_file)

        print(f'Created {output_path}')