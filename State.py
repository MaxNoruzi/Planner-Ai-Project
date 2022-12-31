class State:
    def __init__(self, parent, action, positive_literals, negative_literals):
        self.parent = parent
        self.action = action

        self.positive_literals = []
        self.negative_literals = []

        for positive_literal in positive_literals:
            self.positive_literals.append(positive_literal)

        for negative_literal in negative_literals:
            self.negative_literals.append(negative_literal)

    def to_string(self):
        return f'state, positive literals: {self.positive_literals}, negative literals: {self.negative_literals}'

    def hash(self):
        hash = ""

        i = 0
        j = 0

        while i < len(self.positive_literals) and j < len(self.negative_literals):
            if self.positive_literals[i] <= self.negative_literals[j]:
                hash += self.positive_literals[i]
                i += 1
            else:
                hash += self.negative_literals[j]
                j += 1

        while i < len(self.positive_literals):
            hash += self.positive_literals[i]
            i += 1
        
        while j < len(self.negative_literals):
            hash += self.negative_literals[j]
            j += 1

        return hash