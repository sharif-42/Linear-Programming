from pulp import LpProblem, LpMaximize, LpVariable, value

# Initialize model
model = LpProblem("Maximize Backery Profit", sense=LpMaximize)

# Define decision variables
# How may A and B cakes are produced.
A = LpVariable("A", 0, cat="Integer")
B = LpVariable("B", 0, cat="Integer")

# Define Objective Function
model += 20 * A + 40 * B

# Define Constraints
model += 0.5 * A + 1 * B <= 30
model += 1 * A + 2.5 * B <= 60
model += 1 * A + 2 * B <= 22

# Solve Model
model.solve()
print(f"Product {A.varValue} cake A")
print(f"Product {B.varValue} cake B")
print(f"Profit = {value(model.objective)}")

# The problem data is written to an .lp file
model.writeLP("bakery-resource-scheduling/bakery-resource-scheduling.lp")

