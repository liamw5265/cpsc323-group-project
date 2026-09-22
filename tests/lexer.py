from src.lexer import (identifier_fsm, 
                       starting_state, 
                       identifier_accepting_states, 
                       identifier_transition_function)

# run "python -m tests.lexer" in root file to view tests

print('Identifier FSM test')
identifier_test_inputs = ['hello', 'HELLO', 'Hello', 'he11o', '1hello', 'hello_', 'he_1l0', '_hello']
for string in identifier_test_inputs:
    if (identifier_fsm(string,
                       starting_state,
                       identifier_accepting_states,
                       identifier_transition_function)):
        print(f'{string} --> valid identifier')
    else:
        print(f'{string} --> invalid identifier')