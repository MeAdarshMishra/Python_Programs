l=((2,5),(1,2),(4,4),(2,3),(2,1))
l1=list(l)
l2=[]
for i in l1:
    
    l2.append(i[-1])
    l2.sort()
print(l2)
