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


