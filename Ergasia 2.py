#hi again proffessor here is my second excercise with python i don't expect it o be perfect but it works as far as i am concerned
#the "a" varible is the input, i know you said we could make it with a standard input but i wanted it to be more realistic
a=raw_input("Vale tis parentheseis pou thes na elenkso: ") 
#"c" on the other hand put the input into a list as i know
c=list(a)
#Whilist "e" counts the letters of the "c" list
e=len(c)
#The "p" variable is a counter you will see later what i use it for, i will explain
p=0
#with this "if" i see whether or the parenthesis starts with ")" cause then it is surely wrong and so i don't need to check anything else 
if c[0]==")" :
    print ("False")
else:
    for i in range (e):
        #so regarding the "p" variable as i said it's a counter, every time it sees a parenthesis open it goes up by 1
        if c[i]=="(":
            p+=1
        else :
            #but when it sees a parenthesis close it goes down by 1
            p-=1
        if p<=-1:
            #So this is the thing that i was looking for the whole time. If i see a parenthesis close while the "p" variable is 0(that means there is no open parenthesis) then everything is wrong so the "for" breaks
            break
    #At the end he i see if "p" is zero so every parenthesis that opened close          
    if p==0 :
        print True
    else:
        #if not i print flase as you said
        print False
        
