from pulp import LpProblem, LpMaximize, LpVariable, value, PULP_CBC_CMD

# Initialize model
model = LpProblem("Maximize_Dining_Profit", sense=LpMaximize)

# Defining variables
X1 = LpVariable("Bowdoin_Log", 0, cat="Integer")
X2 = LpVariable("Chocolate_Cake", 0, cat="Integer")

# Define Objective Function
model += 10 * X1 + 5 * X2

# Check how objectives are represented
print("Objective", model.objective)

# Defining Constraints
# model += 5 * X1 + 1 * X2 <= 90
# model += 1 * X1 + 10 * X2 <= 300
# model += 4 * X1 + 6 * X2 <= 125

# These constraints can be written as
model += (5 * X1 + 1 * X2 <= 90, "Oven_constraints")
model += (1 * X1 + 10 * X2 <= 300, "Food_constraints")
model += (4 * X1 + 6 * X2 <= 125, "Boiler_constraints")


# Check how constraints are represented
print("Constraints", model.constraints)

# Solve Model
# status = model.solve()
# IF you don't want unwanted solver messages
status = model.solve(PULP_CBC_CMD(msg=0))

print("Status", status)
# 1: optimal, 2: not solved, 3: infeasible, 4: unbounded, 5: undefined

print(f"Product {X1.varValue} Bowdoin Log")
print(f"Product {X2.varValue} Chocolate Cake")
print(f"Profit = {value(model.objective)}")

# The problem data is written to an .lp file
model.writeLP("dining_production_problem/dining_production.lp")
