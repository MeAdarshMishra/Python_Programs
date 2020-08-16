n=int(input("Upto How many terms"))
n1,n2=0,1
count=0
if n<=0:
    print("Please enter a valid integer")
elif n==1:
    print("FIbonacci series sequence upto",n,":")
    print(n1)
else:
    print("Fibonacci sequences:")
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    
      
