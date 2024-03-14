# Dining Production Problem

## Problem Definition
A dining is producing Bowdoin Log and Chocolate Cake.

- Each Bowdoin Log has satisfaction of 10(or price $10)
- Each Chocolate Cake has satisfaction of 5.

<b>How many Bowdoin logs and chocolate cakes should dining hall make to maximize profit?</b>

For each item the chef needs to use an oven a food processor and a boiler.

|                | Processing time per log | Processing time per cake | Total available time |
|----------------|-------------------------|--------------------------|----------------------|
| Oven           | 5 min                   | 1 min                    | 90 min               |
| Food processor | 1 min                   | 10 min                   | 300 min              |
| Boiler         | 4 min                   | 6 min                    | 125 min              |

## Solution
maximixe Z=10*X1+5*X2 

X1=Number of Bowdoin log and 10 is price 
X2=Number of Chocolate cake and 5 is price

### Subject to or Constraints
- X1>=0 (Log could be produced)
- X2>=0 (Cake could be produced)
- 5*X1+1*X2<=90 (Using time of Oven)
- 1*X1+10*X2<=300 (Using time of food processor)
- 4*X1+6*X2<=125 (Using time of Boiler)


