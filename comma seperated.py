l=list(map(int,input().split()))
for i in l:
    c=0
    for j in range(2,i):
        if(i%j)==0:
            c=1
            break
    if(c==0):
        l.remove(i)
print(l)                
            
