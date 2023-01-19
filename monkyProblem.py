from Action import Action


def get_actions():
    actions = []

    # tires = ["spare", "flat"]
    height=["LOW","HIGH"]
    locations = ["A", "B","C"]

    for loc in locations:
        for h in height:
            for loc1 in locations:
        # put_action = Action(name="put" + tire + "axle", positive_preconditions=["at" + tire + "ground"], \
        #                       negative_preconditions=["atflataxle", "atspareaxle"], add_list=["at" + tire + "axle"], \
        #                       delete_list=["at" + tire + "ground"])
                go_action = Action(name="go" + loc + "Box", positive_preconditions=["at" + loc + "Monkey","Height Monkey ="+height], \
                                    negative_preconditions=[loc!=loc1], add_list=["at" +  "Monkey" + loc1], \
                                    delete_list=["not at"  + "Monkey"+ loc])
            actions.append(go_action)
        for location in locations:
            remove_action = Action(name="rem" + tire + location, positive_preconditions=["at" + tire + location], \
                                   negative_preconditions=[], add_list=["at" + tire + "ground"], delete_list=["at" + tire + location])
            actions.append(remove_action)

    return actions