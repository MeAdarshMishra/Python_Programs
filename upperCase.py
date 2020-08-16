a='Adarsh'
b=''
for i in a:
    if i.islower()==True:
        c=i.upper()
        b=b+c
    elif i.isupper()==True:
        c=i.lower()
        b=b+c
print(b)
