from State import State


def forward_search(goal_state, initial_state, actions):
    fringe = [initial_state]



def get_successors(state, actions):
    result = []
    for action in actions:
    # write your code here
        pass        
    return result


def goal_test(state, initial_state):
    # write your code here
    return


def print_solution(state):
    while True:
        if state.action == None or state.parent == None:
            break
        print(state.action.to_string())
        state = state.parent