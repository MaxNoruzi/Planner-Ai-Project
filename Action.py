from State import State
class Action:
    def __init__(self, name, positive_preconditions, negative_preconditions, add_list, delete_list):
        self.name = name
        self.positive_preconditions = positive_preconditions
        self.negative_preconditions = negative_preconditions
        self.add_list = add_list
        self.delete_list = delete_list

    def regress(self, state: State):
        #hazf effect + precondition haye hazf shode ro ezafe mikonim ta state ghablio bede (parent) 
        #state migire -> tori updatesh mikonim ke beshe state ghabli
        for add in self.add_list:
            if add in state.positive_literals:
                state.positive_literals.remove(add)
        state.positive_literals = list(set(state.positive_literals) | set(self.positive_preconditions))
        state.positive_literals =  list(set(state.positive_literals))
        for dell in self.delete_list:
            if dell in state.negative_literals:
                state.negative_literals.remove(dell)

        state.negative_literals = list(set(state.negative_literals) | set(self.negative_preconditions))
        state.negative_literals =  list(set(state.negative_literals))
        state.action = self
        return

    def is_relevant(self, state):
        if not self.is_unified(state):
            return False

        if self.is_conflicting(state):
            return False

        return True

    def is_unified(self, state):
        for pos in state.positive_literals:
            for pos2 in self.positive_preconditions:
                if pos == pos2:
                    return True
        return False

    def is_conflicting(self, state):
        for neg in state.negative_literals:
            for pod in self.positive_preconditions:
                if neg ==pod:
                    return True
        return False

    def to_string(self):
        return f'action, name: {self.name}, positive preconditions: {self.positive_preconditions}, negative preconditions: {self.negative_preconditions}, add list: {self.add_list}, delete list: {self.delete_list}'