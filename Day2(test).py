# Check if a number is positive, negative, or zero.

num = int(input("Enter a number :"))
if num > 0:
    print(f"{num} is Positive")
elif num == 0:
    print(f"Zero")
else:
    print(f"{num} is Negative")
    
# Check if a year is a leap year.

num = int(input("Enter year :"))
if num % 4 == 0:
    print(f"{num} is Leap year")
else:
    print(f"{num} is not Leap year")

# Check if a number is divisible by 5 and 11.

num = int(input("Enter number :"))
if num % 5 == 0:
    print(f"{num} is divisible by 5.")
elif num % 11 == 0:
    print(f"{num} is divisible by 11.")
else:
    print(f"{num} is not divisible by 5 and 11.")

 
# Print the largest of three numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Largest number is:", max(a, b, c))
 
 
# Build a simple grading system.

num = int(input("Enter marks :"))
if num >= 90 and num == 100:
    print("A+ grade")
elif 90 > num >= 80:
    print("A grade")
elif 80 > num >= 70:
    print("B grade")
elif 70 > num >= 60:
    print("C grade")
elif 60 > num >= 50:
    print("D grade")
else:
    print("F grade")
 
 
# Check eligibility to vote.

age = int(input("Enter age :"))
if age > 18 or age == 18:
    print("You are eligible voter.")
else:
    print("You are not eligible voter.")