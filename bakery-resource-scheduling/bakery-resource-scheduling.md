## Bakery Resource Scheduling

### Problem Definition.

Consultant of boutique cake bakery that sells two types of cake.

- 30 days month
- There is
    - One Oven
    - 2 Bakers
    - 1 packer Only works 22 days per month.

#### Resources are like

|         | Cake A   | Cake B   |
|---------|----------|----------|
| Oven    | 0.5 days | 1 day    |
| Backers | 1 day    | 2.5 days |
| Packers | 1 day    | 2 days   |

#### Profit

|        | Cake A | Cake B |
|--------|--------|--------|
| Profit | $20.00 | $40.00 |

### Solutions

#### Objective.

The Objective will be maximizing the profit. Profit=20*A+40*B (A=Cake_A, B=Cake-B)

#### Subject to or Constraints

- A>=0
- B>=0
- 0.5A+1B <=30
- 1A+2.5B <=60 (as 2 backers)
- 1A+2B<=22 (as packers only work for 22 days per month)

### Common Modeling process of PuLP

- Initializing the model,
- Defining the decision variables,
- Defining the objective function,
- Defining the model constraints,
- Solve Model