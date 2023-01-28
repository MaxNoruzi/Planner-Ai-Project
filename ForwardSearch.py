from queue import PriorityQueue

from State import State


def forward_search(goal_state, initial_state, actions):
    fringe = [initial_state]
    in_fringe = [initial_state.hash()]
    explored = []

    while fringe:
        current_state = fringe.pop(0)
        in_fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors(current_state, goal_state, actions)

        for successor in successors:
            if goal_test(successor, goal_state):
                print_solution(successor)
                return
            else:
                if successor.hash() not in in_fringe and successor.hash() not in explored:
                    fringe.append(successor)
                    in_fringe.append(successor.hash())

def forward_search_heuristic(goal_state, initial_state, actions):
    fringe = PriorityQueue()
    fringe.put(initial_state)
    in_fringe = [initial_state.hash()]
    explored = []

    while not fringe.empty():
        current_state = fringe.get(0)
        in_fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors(current_state, goal_state, actions)

        for successor in successors:
            if goal_test(successor, goal_state):
                print_solution(successor)
                return
            else:
                if successor.hash() not in in_fringe and successor.hash() not in explored:
                    fringe.put(successor)
                    in_fringe.append(successor.hash())

def get_successors(state, goal, actions):
    result = []
    for action in actions:
        if action.is_relevantForward(state):
            successor=State(state,action,state.positive_literals,state.negative_literals)
            action.progress(successor)
            successor.heuristic = ignorePreconditions(successor, goal)
            result.append(successor)      
    return result

def ignorePreconditions(state, goal):
    cost = 0
    for pos in goal.positive_literals:
        if pos not in state.positive_literals:
            cost += 1

    for pos in goal.positive_literals:
        if pos in state.negative_literals:
            cost += 1
    return cost 
    
def ignoreDeleteList(state, goal):
    cost = 0
    for p in goal.positive_literals:
        if p not in state.positive_literals:
            cost += 1
    return cost


def goal_test(state, goal_state):
    for positive_literal in goal_state.positive_literals:
        if positive_literal not in state.positive_literals:
            return False
        
    for positive_literal in goal_state.positive_literals:
        if positive_literal in state.negative_literals:
            return False
        
    return True


def print_solution(state):
    if state.action == None or state.parent == None:
        return
    print_solution(state.parent)
    print(state.action.to_string())