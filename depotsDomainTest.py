from BackwardSearch import backward_search
from ForwardSearch import forward_search
from State import State
from depotsdomain import get_actions


def main():
    print("Getting the set of all actions...")
    actions = get_actions()

    print("Planning...")

   
    initial_state = State(None, None, positive_literals=['TruckAt1', 'BoxBAt1','Bplate5','clearB'], negative_literals=[])
    goal_state = State(None, None, positive_literals=['Bonfloor'], negative_literals=[])
    backward_search(goal_state, initial_state, actions)
    # forward_search(goal_state, initial_state, actions)
if __name__ == "__main__":
    main()
