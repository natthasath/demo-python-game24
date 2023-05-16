import itertools

class Game24Solver:
    def __init__(self, numbers):
        self.numbers = numbers
        self.operators = ['+', '-', '*', '/']
        
    def solve(self):
        perms = list(itertools.permutations(self.numbers))
        
        for perm in perms:
            for ops in itertools.product(self.operators, repeat=3):
                expression = '(((%s %s %s) %s %s) %s %s)' % (perm[0], ops[0], perm[1], ops[1], perm[2], ops[2], perm[3])
                
                try:
                    result = eval(expression)
                    if result == 24:
                        return expression
                except ZeroDivisionError:
                    pass
                
        return "No solution found."