number= int(input("Enter a number: "))

if number%2==0:
    if number%3==0:
        print("Divisible by both 2 and 3")
    else:
        print("Divisible by 2 but not 3")
elif number%3==0:
    print("Divisible by 3 but not 2")
else:
    print("Not divisible by both 2 and 3")
