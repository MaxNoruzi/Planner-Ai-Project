import time

from BackwardSearch import backward_search
# from tireproblem import get_actions
from blockworlds import get_actions
from ForwardSearch import forward_search, forward_search_heuristic
from State import State


def main():
    print("Getting the set of all actions...")
    print("Planning...")
    # initial_state = State(None, None, positive_literals=['atflataxle', 'atsparetrunk'], negative_literals=['atspareaxle', 'atspareground', 'atflatground'])
    # goal_state = State(None, None, positive_literals=['atspareaxle', 'atflatground'], negative_literals=['atsparetrunk', 'atspareground', 'atflataxle'])
    # actions = [Action("Generic", positive_preconditions=["A", "B"], negative_preconditions=[], add_list=["C"], delete_list=[]), \
    # Action("Generic", positive_preconditions=["B", "C"], negative_preconditions=[], add_list=["D"], delete_list=[])]

    # start = time.time()
    # backward_search(goal_state, initial_state, actions)
    # forward_search(goal_state, initial_state, actions)
    # forward_search_heuristic(goal_state, initial_state, actions)
    # print(time.time() - start)

    #Testing block worlds
    # init = State(None, None, positive_literals=['onATable', 'onBTable', 'onCA', 'blockA', 'blockB', 'blockC', 'clearB', 'clearC', 'clearTable'], negative_literals=[])
    # goal = State(None, None, positive_literals=['onAB', 'onBC'], negative_literals=[])
    init = State(None, None, positive_literals=['onATable', 'onBTable', 'onCA','onDB', 'blockA', 'blockB', 'blockC','blockD', 'clearD', 'clearC', 'clearTable'], negative_literals=[])
    goal = State(None, None, positive_literals=['onAB', 'onBC', 'onCD'], negative_literals=[])
    blocks = []
    for p in init.positive_literals:
        if 'block' in p:
            blocks.append(p[-1])
    actions = get_actions(blocks)
    forward_search_heuristic(goal, init, actions)
if __name__ == "__main__":
    main()
