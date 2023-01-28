from BackwardSearch import backward_search
from ForwardSearch import forward_search
from State import State
from monkyProblem import get_actions


def main():
    print("Getting the set of all actions...")
    actions = get_actions()

    print("Planning...")
    positive_literals = ["atMonkeyA", "atBananaB", "atBoxC", "heightMonkeyLow", "heightBoxLow", "heightBananaHigh",
                         "pushableBox", "climbableBox", "graspableBanana", "notEqualAB", "notEqualAC", "notEqualBA", "notEqualBC", "notEqualCA", "notEqualCB"]
    initial_state = State(
        None, None, positive_literals=positive_literals, negative_literals=[])

    goal_literal = ["haveMonkeyBanana"]
    goal_state = State(
        None, None, positive_literals=goal_literal, negative_literals=[])

    backward_search(goal_state, initial_state, actions)
    # forward_search(goal_state, initial_state, actions)


if __name__ == "__main__":
    main()
