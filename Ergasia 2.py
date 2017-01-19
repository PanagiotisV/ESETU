a=raw_input("Vale tis parentheseis pou thes na elenkso: ") 
c=list(a)
e=len(c)
p=0

if c[0]==")" :
    print ("False")
else:    
    for i in range (e):
        if c[i]=="(":
            p+=1
        else :
            p-=1
        if p<=-1:
            break
    if p==0 :
        print True
    else:
        print False
        
