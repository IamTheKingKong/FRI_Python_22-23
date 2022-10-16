"""
Mandatory part
Ships need fuel. The required amount depends upon the weight of the cargo. "Instructions for use" state that it goes
like this: divide the cargo weight by 3, round down to an integer and subtract two. Repeat. Repeat. Repeat ...
The amount of fuel equals the number of steps needed to reach 0 or a negative number.

For example, let the cargo weight 756 tons.

756 / 3 - 2 = 250
250 / 3 - 2 = 81
81 / 3 - 2 = 25
25 / 3 - 2 = 6
6 / 3 - 2 = 0
We need five steps to reach 0, so we need 5 tons of fuel.

Write a program into which we enter the weight of the cargo, and it computes the required quantity of fuel. If we enter
756, it prints 5. If we enter 100756, it prints 10.

Extra task
Ooops, we misread the instructions. (No wonder: we bought the ship on Ali Express for $35, free shipping, and English
instructions were just terrible.) It actually goes like this: for 756 tons of cargo, we need 756 / 3 - 2 = 250 tons of
fuel. However, this fuel also need to be carried, so we need additional 250 / 3 - 2 = 81 tons of fuel to carry this
fuel. And so forth. In total, we need 250 + 81 + 25 + 6 = 362 tons of fuel.

Add this computation to your program, so that it also outputs the number computed in this way. If we enter 756, it
prints 5 (as before) and then 362. If we enter 100756, it prints 10 (as before) and then 50346.

Note: yes, I know, this ship is really inefficient. (What did we expect from Ali Express?) And also: yes, the ship
doesn't carry 756 t of fuel all the way. It burns it and is thus lighter and lighter. But we don't want to complicate
the task too much, do we?
"""

cargo_weigth = int(input("Enter the weight of the cargo: "))

fuel_quantity = 0  # Mandatory Task
corected_fuel_cuantity = 0

while cargo_weigth > 0:
    cargo_weigth = cargo_weigth // 3 - 2
    fuel_quantity += 1
    if cargo_weigth > 0:
        corected_fuel_cuantity += cargo_weigth

print("Fuel Quantity: " + str(fuel_quantity))
print("Corected Fuel Quantity: " + str(corected_fuel_cuantity))
