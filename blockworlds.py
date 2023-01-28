from Action import Action


def get_actions(blocks):
    actions = []

    blocks.append('Table')

    for b1 in blocks:
        for b2 in blocks:
            for b3 in blocks:
                if b1 != 'Table' and b3 != 'Table' and b1 != b2 and b1 != b3 and b2 != b3:
                    move_action = Action(name='move ' + b1 + ' from ' + b2 + ' on ' + b3, 
                        positive_preconditions=['on' + b1 + b2, 'clear' + b1, 'clear' + b3, 'block' + b1, 'block' + b3],
                    negative_preconditions=[], add_list=['on' + b1 + b3, 'clear' + b2], 
                    delete_list=['on' + b1 + b2, 'clear' + b3])
                    actions.append(move_action)
            if b1 != 'Table' and b2 != 'Table':
                move_table_action = Action(name='move ' + b1 + ' from ' + b2 + ' on Table', 
                        positive_preconditions=['on' + b1 + b2, 'clear' + b1, 'block' + b1, 'block' + b2],
                negative_preconditions=[], add_list=['on' + b1 + 'Table', 'clear' + b2], 
                delete_list=['on' + b1 + b2])
                actions.append(move_table_action)


    return actions