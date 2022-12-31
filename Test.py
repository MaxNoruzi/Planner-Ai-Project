from State import State
from BackwardSearch import backward_search
from tireproblem import get_actions
def main():
    print("Getting the set of all actions...")
    actions = get_actions()

    print("Planning...")
    initial_state = State(None, None, positive_literals=["atflataxle", "atsparetrunk"], negative_literals=[])
    goal_state = State(None, None, positive_literals=["atspareaxle"], negative_literals=[])
    # actions = [Action("Generic", positive_preconditions=["A", "B"], negative_preconditions=[], add_list=["C"], delete_list=[]), \
    # Action("Generic", positive_preconditions=["B", "C"], negative_preconditions=[], add_list=["D"], delete_list=[])]
    backward_search(goal_state, initial_state, actions)
if __name__ == "__main__":
    main()
