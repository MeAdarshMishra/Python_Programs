#3.wap to find whether a given number is odd or even only by using bitwise operator.
n=int(input("Enter a number check even or odd"))
if(n&1):
    print("Odd Number")
else:
    print("Even number")
