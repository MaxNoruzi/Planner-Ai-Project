from State import State


class Action:
    def __init__(self, name, positive_preconditions, negative_preconditions, add_list, delete_list):
        self.name = name
        self.positive_preconditions = positive_preconditions
        self.negative_preconditions = negative_preconditions
        self.add_list = add_list
        self.delete_list = delete_list

    def regress(self, state: State):
        for add in self.add_list:
            if add in state.positive_literals:
                state.positive_literals.remove(add)
        
        for pos in self.positive_preconditions:
            if pos not in state.positive_literals:
                state.positive_literals.append(pos)
        
        for delete in self.delete_list:
            if delete in state.negative_literals:
                state.negative_literals.remove(delete)
        
        for neg in self.negative_preconditions:
            if neg not in state.negative_literals:
                state.negative_literals.append(neg)

    def progress(self, state):
        for add in self.add_list:
            if add not in state.positive_literals:
                state.positive_literals.append(add)

        for delete in self.delete_list:
            if delete in state.positive_literals:
                state.positive_literals.remove(delete)
        
        for delete in self.delete_list:
            if delete not in state.negative_literals:
                state.negative_literals.append(delete)

        for add in self.add_list:
            if add in state.negative_literals:
                state.negative_literals.remove(add)

    def is_relevant(self, state):
        if not self.is_unified(state):
            return False

        if self.is_conflicting(state):
            return False

        return True

    def is_unified(self, state):
        for pos in state.positive_literals:
            if pos in self.add_list:
                return True
        for neg in state.negative_literals:
            if neg in self.delete_list:
                return True
        return False

    def is_conflicting(self, state):
        for pos in state.positive_literals:
            if pos in self.delete_list:
                return True
        for neg in state.negative_literals:
            if neg in self.add_list:
                return True
        return False
    
    def is_relevantForward(self, state):
        for pos in self.positive_preconditions:
            if pos not in state.positive_literals:
                return False
        
        for neg in self.negative_preconditions:
            if neg not in state.negative_literals:
                return False
            
        for pos in self.positive_preconditions:
            if pos in state.negative_literals:
                return False
        
        for neg in self.negative_preconditions:
            if neg in state.positive_literals:
                return False
        
        return True

    def to_string(self):
        return f'action, name: {self.name}, positive preconditions: {self.positive_preconditions}, negative preconditions: {self.negative_preconditions}, add list: {self.add_list}, delete list: {self.delete_list}'