from Action import Action


def get_actions():
    actions = []

    heights = ["LOW", "HIGH"]
    locations = ["A", "B", "C"]
    objects = ["Box", "Banana"]

    # add actions for moving the monkey
    for x in locations:
        for y in locations:
            if x == y:
                continue

            go_action = Action(
                name=f"go{x}{y}",
                positive_preconditions=[
                    f"atMonkey{x}", f"heightMonkeyLOW", f"notEqual{x}{y}"],
                negative_preconditions=[],
                add_list=[f"atMonkey{y}"],
                delete_list=[f"atMonkey{x}"]
            )
            actions.append(go_action)

    # add actions for pushing the object
    for x in locations:
        for y in locations:
            for obj in objects:
                if x == y:
                    continue

                push_action = Action(
                    name=f"push{obj}{x}{y}",
                    positive_preconditions=[
                        f"atMonkey{x}", f"heightMonkeyLOW", f"at{obj}{x}", f"pushable{obj}", f"height{obj}LOW", f"notEqual{x}{y}"],
                    negative_preconditions=[],
                    add_list=[f"at{obj}{y}", f"atMonkey{y}"],
                    delete_list=[f"at{obj}{x}", f"atMonkey{x}"]
                )
                actions.append(push_action)

    # add actions for climbing the object
    for x in locations:
        for obj in objects:
            climb_action = Action(
                name=f"climbUp{x}{obj}",
                positive_preconditions=[
                    f"atMonkey{x}", f"heightMonkeyLOW", f"at{obj}{x}", f"climbable{obj}", f"height{obj}LOW"],
                negative_preconditions=[],
                add_list=[f"onMonkey{obj}", f"heightMonkeyHIGH"],
                delete_list=[f"heightMonkeyLOW"]
            )
            actions.append(climb_action)

    # add actions for grasping the object
    for x in locations:
        for obj in objects:
            for height in heights:
                grasp_action = Action(
                    name=f"grasp{x}{obj}{height}",
                    positive_preconditions=[
                        f"atMonkey{x}", f"heightMonkey{height}", f"at{obj}{x}", f"graspable{obj}", f"height{obj}{height}"],
                    negative_preconditions=[],
                    add_list=[f"haveMonkey{obj}"],
                    delete_list=[f"at{obj}{x}", f"height{obj}{height}"]
                )
                actions.append(grasp_action)

    return actions
