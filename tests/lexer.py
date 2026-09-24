from src.lexer import (fsm, 
                       starting_state, 
                       identifier_accepting_states, 
                       identifier_transition_function,
                       real_accepting_states,
                       real_transition_function,
                       integer_accepting_states,
                       integer_transition_function)

# run "python -m tests.lexer" in root file to view tests

print('Identifier FSM test')
identifier_test_inputs = ['hello', 'HELLO', 'Hello', 'he11o', '1hello', 'hello_', 'he_1l0', '_hello']
for string in identifier_test_inputs:
    if (fsm(string,
            starting_state,
            identifier_accepting_states,
            identifier_transition_function)):
        print(f'{string} --> valid identifier')
    else:
        print(f'{string} --> invalid identifier')

print('Real FSM test')
real_test_inputs = ['0.11', '0.9l', '10.11', '.111', '.lll', '0.1_1', '1111', '1.00']
for string in real_test_inputs:
    if (fsm(string,
            starting_state,
            real_accepting_states,
            real_transition_function)):
        print(f'{string} --> valid real')
    else:
        print(f'{string} --> invalid real')

print('Integer FSM test')
integer_test_inputs = ['100', 'l00', '0', ' ', '1.00', '1_0', '.01', '2']
for string in integer_test_inputs:
    if (fsm(string,
            starting_state,
            integer_accepting_states,
            integer_transition_function)):
        print(f'{string} --> valid integer')
    else:
        print(f'{string} --> invalid integer')