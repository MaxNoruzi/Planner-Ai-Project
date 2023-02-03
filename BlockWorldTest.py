from BackwardSearch import backward_search
from ForwardSearch import forward_search
from State import State
from blockworlds import get_actions

def main():
    print("Getting the set of all actions...")

    print("Planning...")

# goal = State(None, None, positive_literals=['onAB', 'onBC'], negative_literals=[])
    init = State(None, None, positive_literals=['onATable', 'onBTable', 'onCA','onDB', 'blockA', 'blockB', 'blockC','blockD', 'clearD', 'clearC', 'clearTable'], negative_literals=[])
    goal = State(None, None, positive_literals=['onAB', 'onBC', 'onCD'], negative_literals=[])
    blocks = []
    for p in init.positive_literals:
        if 'block' in p:
            blocks.append(p[-1])
    actions = get_actions(blocks)
    forward_search(goal, init, actions)
if __name__ == "__main__":
    main()
