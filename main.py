import tweepy
import random

#consumer_key = "IWoCpSOeWXJackdRPksc5y3en"
#consumer_secret = "8yv1rP8lppmpDLl9OyRpON7VuoLl2wyX4mupIECpQ88idd6lgF"
#access_token = "923171211324088320-SciHc7VDOkaMNtfabkBpEZtxb9ufhHa"
#access_token_secret = "Yw6CHQIn4U5zMBmSCPZWYNs8LdgxAzxCMUDmPzxt4lgat"

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth)

chars = [ ['q','w','e','r','t','y','u','i','o','p'], ['a','s','d','f','g','h','j','k','l'], ['z','x','c','v','b','n','m'] ]
boris_nouns = ["betchup", "spidder", "kid", "Bread", "children", "salad", "space jam","allabama","bible","chikcen","dad","dream","soup","cheek","cheeks","bird","snake","cheeese","berrris","berrries","berrys","meat","mellon","melon","allemabama","cake"]
boris_names = ["Michael B. Jordan", "@GOP", "@realDonaldTrump", "@CNN", "@mike_pence", "@SenBobCasey","@AjitPaiFCC","@comcast","@tedcruz"]
boris_openers =["", "uh oh,","bopen","YO","faceroll","ayo,","RED ALERT:","heyo","Sometimes",]
boris_good_adjectives =["tasty","big","meaty","teasty","yummy","fruitful","warm","green","ggreat","greate","greatt","cool","toasty","toastey"]
boris_bad_adjectives =["damp","dammp","dry","dusty","red","uggly","ugley","uggley","mush","cold","weak","sticky","stinkky","wet"<"bad"]
boris_past_verbs =["dropped","ate","saw","popped","slid","had a dream about","licked","produced","cleaned","rubbed","smacked","bopped"]
boris_do_verbs =["drop","eat","pop","lick","rub","slide","dislike","smack","bop"]

def faceroll():
    roll = ''
    length = random.randint(10, 40)
    row = random.randint(0, 2)
    col = random.randint(0, (len(chars[row]) - 1))
    for i in range(length):
        roll += chars[row][col]
        row = changeRow(row)
        col = changeColumn(row, col)
    if random.random() > 0.5:
        return roll.upper()
    else:
        return roll



def changeRow(row):
    if random.random() < 0.25:
        return row
    elif random.random() < 0.375:
        if row + 1 > 2:
            return row 
        else:
            return row + 1
    else:
        if row == 0:
            return row
        else:
            return row - 1

def changeColumn(row, col):
    if random.random() < 0.25:
        if col >= len(chars[row]):
            return len(chars[row]) - 1
        else:
            return col
    elif random.random() < 0.375:
        if col + 1 >= len(chars[row]):
            return len(chars[row]) - 1 
        else:
            return col + 1
    else:
        if col == 0:
            return col
        else:
            return row - 1

def bopen():
    bbb = ''
    length = random.randint(15,60)
    for i in range(length):
        if random.random() > 0.07:
            bbb += "b"
        else:
            bbb += " "
    return bbb


def bweet():
    bbb = ''
    length = random.randint(10,200)
    for i in range(length):
        if random.random() > 0.05:
            bbb += "b"
        elif random.random() > 0.98:
            bbb += "\n"
        else:
            bbb += " "
    return bbb

def gensen():
    sen = boris_openers[random.randint(0, len(boris_openers) - 1)]
    if sen == "bopen":
        sen = bopen() + " "
    if sen == "faceroll":
        sen = faceroll() + " "
    if sen == "":
        if random.random() > 0.5:
            return boris_nouns[random.randint(0, len(boris_nouns) - 1)]
        else:
            if random.random() > 0.5:
                return boris_bad_adjectives[random.randint(0, len(boris_bad_adjectives) - 1)] + " " + boris_nouns[random.randint(0, len(boris_nouns) - 1)]
            else:
                return boris_good_adjectives[random.randint(0, len(boris_good_adjectives) - 1)] + " " + boris_nouns[random.randint(0, len(boris_nouns) - 1)]
    if "Sometimes" in sen:
        sen += " I" 
    elif random.random() > 0.5:
        sen += " " + boris_names[random.randint(0, len(boris_names) - 1)]
    else:
        sen += " I " + boris_past_verbs[random.randint(0, len(boris_past_verbs) - 1)] + " my " + boris_nouns[random.randint(0, len(boris_nouns) - 1)]
    return sen


if random.random() > 0.75:
    tweet = bweet()
    print(tweet)
elif random.random() > 0.95:
    tweet = "betchup"
    print(tweet)
elif random.random() > 0.75:
    tweet = faceroll()
    print(tweet)
else:
    tweet = gensen()
    print(tweet)