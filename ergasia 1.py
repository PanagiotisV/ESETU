a=raw_input("Vale thn protash gia na vgalo ta thavmastika ") 
c=list(a)
g=len(c)
i=0
while i<g-1:
    if c[i]=="!":
        while c[i]=="!":
            del c[i]
            g-=1
            if i>g-2:
                break
    i+=1
str1 = ''.join(c)
d=len(c)

print str1
