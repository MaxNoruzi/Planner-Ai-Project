from BackwardSearch import backward_search
from ForwardSearch import forward_search
from State import State
from depotsdomain import get_actions


def main():
    print("Getting the set of all actions...")
    actions = get_actions()

    print("Planning...")
    # initial_state = State(None, None, positive_literals=['atflataxle', 'atsparetrunk'], negative_literals=['atspareaxle', 'atspareground', 'atflatground'])
    # goal_state = State(None, None, positive_literals=['atspareaxle', 'atflatground'], negative_literals=['atsparetrunk', 'atspareground', 'atflataxle'])
    initial_state = State(None, None, positive_literals=['TruckAt1', 'BAt1','Bonfloor','AAt2','CAt3','Aplate4','Cplate5'], negative_literals=['AonB', 'BonC'])
    goal_state = State(None, None, positive_literals=['AAt3','BAt3','AonB', 'BonC','Aplate5','Bplate5'], negative_literals=[])
    backward_search(goal_state, initial_state, actions)
    # forward_search(goal_state, initial_state, actions)
if __name__ == "__main__":
    main()
