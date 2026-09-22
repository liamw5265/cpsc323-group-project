identifier_transition_function = {
    'l': {'1': '2', '2': '3', '3': '3', '4': '3', '5': '3', '6': '6'},
    'd': {'1': '6', '2': '4', '3': '4', '4': '4', '5': '4', '6': '6'},
    '_': {'1': '6', '2': '5', '3': '5', '4': '5', '5': '5', '6': '6'}
}

identifier_accepting_states = ['2', '3', '4', '5']

starting_state = '1'

def convert_input_to_identifier_fsm_input(input_str: str) -> str:
    '''
    Turns input into input that the identifier_fsm can accept

    arguments:
        - input_str:

    return (str): New form of input that the identifier_fsm can read
    '''

    result = ''

    for char in input_str:
        if char.isalpha():
            result += 'l'
        elif char.isdigit():
            result += 'd'
        elif char == '_':
            result += '_'
        else:
            result = -1
            break

    return result

def identifier_fsm(input_str: str,
                   starting_states: str,
                   accepting_states: list[str],
                   transition_function: dict[str, dict[str, str]]
                    ) -> bool:
    '''
    Checks [input_str] if it is a valid identifier

    arguments:
        - input_str:
        - starting_stats:
        - accepting_states:
        - transition_function:

    returns (bool): 
    '''

    current_state = starting_states

    for input in input_str:
        next_state = transition_function[input][current_state]
        current_state = next_state

    if current_state in accepting_states:
        return True
    else:
        return False


if __name__ == '__main__':

    input_test = '1he11_o'

    if (identifier_fsm(convert_input_to_identifier_fsm_input(input_test),
                   starting_state,
                   identifier_accepting_states,
                   identifier_transition_function)):
        print('valid identifier')
    else:
        print('invalid identifier')