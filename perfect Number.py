#Perfect Number
n=int(input("Enter a Number."))
sum=0
a=n
while(n>0):
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(sum==a):
    print("Yes")
else:
    print("No")
