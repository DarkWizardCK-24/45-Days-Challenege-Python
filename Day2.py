#if-else loop

# age = 8
# if age >= 18:
#    print("You are eligible to vote.")
# else:
#    print("You are not eligible to vote.")

#if-else loop

# num = int(input("Enter a number: "))
# if num > 0:
#    print("Positive number")
# elif num < 0:
#    print("Negative number")
# else:
#    print("Zero")
    

x = int(input("Enter a number :"))

if x > 0:
    if x % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif x == 0:
    print("Zero")
else: # x < 0
    if x % 2 == 0:
        print("Negative and Even")
    else:
        print("Negative and Odd")
