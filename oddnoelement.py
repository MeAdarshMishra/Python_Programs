l=[1,1,2,3,4,5,6,7,7,7,8,8,9,9]
a=[]
for element in l:
    if((l.count(element))%2!=0):
        a.append(element)
print(a)    
