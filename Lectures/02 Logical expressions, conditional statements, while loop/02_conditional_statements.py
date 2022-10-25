#Lets start with a simple program that calculates BMI (Body Mass Index calculator).

"""weight = float(input("Body Weight: "))
height = float(input("Body Height: "))
bmi = weight / height ** 2
print("Your BMI is: ", bmi)"""

# Now let add to the program statement that checks if the person is overweight

# We check a condition with a IF statement

weight = float(input("Body Weight: "))
height = float(input("Body Height: "))
bmi = weight / height ** 2
print("Your BMI is: ", bmi)
if bmi > 25: #colon after statement
    print("Youz need to loose weight!")

# Nested Statements
