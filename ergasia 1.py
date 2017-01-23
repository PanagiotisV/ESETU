#hello professor this is my first excercise on python i hope you like it :D
#so this is the first input it's a raw_input because it may have words/numbers in it  
a=raw_input("Vale thn protash gia na vgalo ta thavmastika ") 
#here i just put the variable a into a list based on every letter it has 
c=list(a)
#g just counts the letters of the list 
g=len(c)
#i is for the "while" so that i don't get out of the list's variables
i=0
#so "while" counts the i to be less that the amount of variables the list has
while i<g-1:
    #with this "if" here i check if the variable "c[i]" has "!"in it
    if c[i]=="!":
        #now i check if it has more "!" after the first "!" 
        while c[i]=="!":
            del c[i]
            #because every time i delete a variable of the list it gets shorter every time i make the amount of variables less so that i don't get out of the limit of the list
            g-=1
            #now if i am on my last variable i don't need to check it because i want it to stay so i just break the "while" 
            if i>g-2:
                break
    i+=1
#here i reunite the list to make it a sentence again     
str1 = ''.join(c)
print str1
