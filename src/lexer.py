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

keywords_list = ['integer', 'boolean', 'real', 'if', 'else', 'fi', 'while', 'return', 'get', 'put', 'true', 'false', 'function']

separator_list = ['(', ')', '{', '}', ' ', '@', ';', ',', ':']

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
        - input_str:
        - starting_stats:
        - accepting_states:
        - transition_function:

    returns (bool): 
    '''

    new_input_str = convert_input_to_fsm_input(input_str)

    current_state = starting_states

    # Testing
    #print(new_input_str)

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
    '''

    with open(file_path, 'r', encoding = 'utf-8') as file:
        file_contents = file.read()
    print(file_contents)

    input_without_comments = remove_comments(file_contents)
    print(input_without_comments)

    return input_without_comments



def remove_comments(text_input: str) -> str:
    '''
    '''
    inside_comment = False
    input_without_comments = ''

    for index in range(len(text_input) - 1):
        current_char = text_input[index]
        next_char = text_input[index + 1]

        if current_char == comment and not inside_comment and next_char != '=':
            inside_comment = True
        elif current_char == comment and inside_comment and next_char != '=':
            inside_comment = False
        elif not inside_comment:
            input_without_comments += current_char

    return input_without_comments

def separate_tokens(input_str: str) -> list[(str, str)]:
    '''
    '''
    tokens = []



if __name__ == '__main__':
    read_file('tests/test.txt')