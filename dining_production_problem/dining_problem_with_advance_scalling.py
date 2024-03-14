from pulp import LpProblem, LpMaximize, LpVariable, value, PULP_CBC_CMD, lpSum

# Initialize model
model = LpProblem("Maximize_Dining_Profit", sense=LpMaximize)

# Define a dictionary of variables kayed by indices
var_keys = [1, 2]
x = LpVariable.dicts("Bakery_Item", var_keys, lowBound=0, cat="Integer")
print(x)

# Define Objective Function
model += 10 * x[1] + 5 * x[2]

# defining constraints
# model += (5 * x[1] + 1 * x[2] <= 90, "Oven_constraints")
# model += (1 * x[1] + 10 * x[2] <= 300, "Food_constraints")
# model += (4 * x[1] + 6 * x[2] <= 125, "Boiler_constraints")

# model += (lpSum([5 * x[1], 1 * x[2]]) <= 90)
model += (lpSum([1 * x[1], 10 * x[2]]) <= 300)
model += (lpSum([4 * x[1], 6 * x[2]]) <= 125)

# Re-write 1st constraints so that we can handle hundreds on values
coeff = [5, 1]
coeff_dict = dict(zip(var_keys, coeff))
print(coeff_dict)
model+=(lpSum(coeff_dict[i]*x[i] for i in var_keys) <=90)


# Check how constraints are represented
print("Constraints", model.constraints)

# Solve Model
# status = model.solve()
# IF you don't want unwanted solver messages
status = model.solve(PULP_CBC_CMD(msg=0))

print("Status", status)
# 1: optimal, 2: not solved, 3: infeasible, 4: unbounded, 5: undefined

for var in model.variables():
    print(f"{var} = {value(var)}")

# print(f"Product {X1.varValue} Bowdoin Log")
# print(f"Product {X2.varValue} Chocolate Cake")
print(f"Profit = {value(model.objective)}")

# The problem data is written to an .lp file
model.writeLP("dining_production_problem/dining_problem_with_advance_scalling.lp")