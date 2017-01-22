import tweepy
from tweepy import OAuthHandler
import json

consumer_key =  "44Y1xzn3viu3nXaXuxKogqGE5"
consumer_secret =  "IfBiy0fcr5WQ3FlZ35H69SXCeNsrRtIe8vmAujyFlR0qHUpai5"
access_token = '2535514818-aESDMQQiQME133GvWLSRetCQmKdM7kTalw7uH2V'
access_secret = 'O0azOvWfPVaY83juKWSJtyQN2rDIcZ9bhfSB0USaimxPN'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
onoma1=(raw_input('Gimme the first name'))
onoma2=(raw_input('Gimme the second name'))
user = api.get_user(onoma1)
user = api.get_user(onoma2)
a=0
b=0
stuff1 = api.user_timeline(screen_name = onoma1, count = 10)
for tweet in stuff1:
   lekseis1=tweet.text.split(" ")
   a=a+len(lekseis1)
stuff2 = api.user_timeline(screen_name = onoma2, count = 10)
for tweet in stuff2:
   lekseis2=tweet.text.split(" ")
   b=b+len(lekseis2)
if a>b :
    print "Perissoteres lekseis exei o xrhsths:"
    print onoma1
elif a<b :
    print "Perissoteres lekseis exei o xrhsths:"
    print onoma2
else :
    print "exoun tis idies lekseis"

    



