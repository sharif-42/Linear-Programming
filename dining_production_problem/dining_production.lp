\* Maximize_Dining_Profit *\
Maximize
OBJ: 10 Bowdoin_Log + 5 Chocolate_Cake
Subject To
Boiler_constraints: 4 Bowdoin_Log + 6 Chocolate_Cake <= 125
Food_constraints: Bowdoin_Log + 10 Chocolate_Cake <= 300
Oven_constraints: 5 Bowdoin_Log + Chocolate_Cake <= 90
Bounds
 0 <= Bowdoin_Log
 0 <= Chocolate_Cake
Generals
Bowdoin_Log
Chocolate_Cake
End
