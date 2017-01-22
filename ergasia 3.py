p = raw_input('Enter your list: ')
a = eval(p)
b=len(a)
c=[]
for i in range (b):
    if a[i]==0:
        c.append(i)
d=len(c)
for i in range (d):
    e=a.index(0)
    del a[e]
    a.append(0)
print a    

     
