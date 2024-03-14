\* Maximize_Dining_Profit *\
Maximize
OBJ: 10 Bakery_Item_1 + 5 Bakery_Item_2
Subject To
_C1: Bakery_Item_1 + 10 Bakery_Item_2 <= 300
_C2: 4 Bakery_Item_1 + 6 Bakery_Item_2 <= 125
_C3: 5 Bakery_Item_1 + Bakery_Item_2 <= 90
Bounds
 0 <= Bakery_Item_1
 0 <= Bakery_Item_2
Generals
Bakery_Item_1
Bakery_Item_2
End
