from game24.game24 import Game24Solver
import json

with open("set_number.json", "r") as file:
    json_content = file.read()

data = json.loads(json_content)

sets = data["sets"]

for num_set in sets:
    numbers = num_set["numbers"]
    solver = Game24Solver(numbers)
    solution = solver.solve()
    print("Set Number", numbers, "Solution:", solution)

""" # Example usage
numbers = [4, 7, 8, 3]
solver = Game24Solver(numbers)
solution = solver.solve()
print("Solution:", solution) """