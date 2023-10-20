number=int(input("Enter a number:"))
number=str(number)
reverse=number[::-1]

if(reverse==number):
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")


