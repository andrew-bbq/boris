import tweepy

consumer_key = "IWoCpSOeWXJackdRPksc5y3en"
consumer_secret = "8yv1rP8lppmpDLl9OyRpON7VuoLl2wyX4mupIECpQ88idd6lgF"
access_token = "923171211324088320-SciHc7VDOkaMNtfabkBpEZtxb9ufhHa"
access_token_secret = "Yw6CHQIn4U5zMBmSCPZWYNs8LdgxAzxCMUDmPzxt4lgat"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

for status in api.user_timeline(user, "00-00-0000"):
    try:
        status.favorite()
        print("liked")
    except:
        print("already liked")