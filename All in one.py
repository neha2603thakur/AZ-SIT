#1
a=int(input("Enter the number of terms(n) of Fibonacci series:"))
f=0
s=1
print(f,s,end=" ")
for i in range(2,a):
    n=f+s
    print(n,end=" ")
    f=s
    s=n 
print("\n")


#2
print("Prime numbers from 1 to 100 are")
for n in range(2,101):
    f=0
    for i in range(2,n,1):
        if(n%i==0):
            f=1
            
    if(f==0):        
        print(n, end=" ")
print("\n")


#3
number=int(input("Enter a number to check wheather it is palindrome or not:"))
number=str(number)
reverse=number[::-1]

if(reverse==number):
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")
print("\n")


#4
for r in range(1,7):
    for c in range(1,1+r):
        print('*',end=" ")
        
    print("\n")
print("\n")


#5
number= int(input("Enter a number to check weather it is divisible by both 2 and 3 or not: "))

if number%2==0:
    if number%3==0:
        print("It is divisible by both 2 and 3")
    else:
        print("It is divisible by 2 but not 3")
elif number%3==0:
    print("It is divisible by 3 but not 2")
else:
    print("It is not divisible by both 2 and 3")
