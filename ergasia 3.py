#Hmm hi again proffessor this is the 3rd excercise with python i hope you are keeping up with those comments cause they are really usefull (lol) 
#again as with every excercise this is the input i like that raw_input as it can take everything that user has to give to it and then with eval i make it from string into integer 
p = raw_input('Enter your list: ')
#as i said on the input "a" here makes the input an int list 
a = eval(p)
#"b" just counts the numbers in the list as with every other excercise 
b=len(a)
#While "c" here is an empty list you will see later what it is used for
c=[]
for i in range (b):
    #Saying later here we are, every time i see a zero into the list "a" i append it into the "c" list
    if a[i]==0:
        c.append(i)
#hey a len() again, yeah more counting( i don't know if i need to tell you every time i use len() but i am gonna do it anyway cause these are comments and you don't have to read them all)        
d=len(c)
for i in range (d):
    #in order to not loose the amount of zeros the list "a" has i use a "for" 
    #As you probably know index(x) finds the position of the number x in a list so i the programm checks the list for the first zero it finds 
    e=a.index(0)
    #and i delete it from the "a" list 
    del a[e]
    #while also append() it againinto the same list so that it goes on the end of the list without making the other numbers loose their position
    a.append(0)
#At the end i print it 
print a    

     
