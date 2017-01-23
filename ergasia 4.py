import tweepy
from tweepy import OAuthHandler
import json
#hey professor this is my 4th and last excercise :3 i hope you like the other 3
#first of all here i have the keys that you asked for the tweepy to work
consumer_key =  "44Y1xzn3viu3nXaXuxKogqGE5"
consumer_secret =  "IfBiy0fcr5WQ3FlZ35H69SXCeNsrRtIe8vmAujyFlR0qHUpai5"
access_token = '2535514818-aESDMQQiQME133GvWLSRetCQmKdM7kTalw7uH2V'
access_secret = 'O0azOvWfPVaY83juKWSJtyQN2rDIcZ9bhfSB0USaimxPN'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
#While here are the variables onoma1 for the first name and onoma2 for the second one
onoma1=(raw_input('Gimme the first name'))
onoma2=(raw_input('Gimme the second name'))
#here it just checks for these names if they exist
user = api.get_user(onoma1)
user = api.get_user(onoma2)
#These 2 (a,b) keep track of the amount of words each tweet has
a=0
b=0
#Furthermore here are stuff1 and stuff2 which take the tweets of the 1st user name that you gave me
stuff1 = api.user_timeline(screen_name = onoma1, count = 10)
for tweet in stuff1:
   #lekseis1 is a list with all the words of a tweet split by each void before every other word
   lekseis1=tweet.text.split(" ")
   a=a+len(lekseis1)
#stuff2 does the same job as stuff1 but for the 2nd variable   
stuff2 = api.user_timeline(screen_name = onoma2, count = 10)
for tweet in stuff2:
   #the same with lekseis1
   lekseis2=tweet.text.split(" ")
   b=b+len(lekseis2)
#now here i just check the 2 variables  (a,b) to see wich one has the biggest number in it
if a>b :
    print "Perissoteres lekseis exei o xrhsths:"
    print onoma1
elif a<b :
    print "Perissoteres lekseis exei o xrhsths:"
    print onoma2
else :
    print "exoun tis idies lekseis"
#i hope you liked it and that it was right qB^) bye
    



