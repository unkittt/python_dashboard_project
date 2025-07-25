import tweepy
import schedule
import time
import random

# Twitter API credentials for multiple accounts
accounts = [
    {
        'consumer_key': 'r8DBuE6Azj9kKTEcC9VR0b0uL',
        'consumer_secret': 'ubtlESnQq1ggaixA7Su9UPGpET1m8fSvILhwnIbKoDLn04WY8h',
        'access_token': '1945448277589237760-2hOLnQoQOvDX5ejGGwN2JN4fD4X77N',
        'access_token_secret': '3SmANN3TD7mFipknQScxLjE2zZRDOYUDbLPslm4phSllL'
    },
    # Add more accounts like this if needed
]

# List of tweets to choose from
content_list = [
    "Subah ki chai, halka sa baarish ka mausam, aur ek chhoti si muskaan! #AajKeAcheDin",
    "Isi tarah shuru hote hain ache din. #AajKeAcheDin",
    "Aapke ache din kaise guzar rahe hain? #AajKeAcheDin",
    "Daily gratitude ka magic #AajKeAcheDin",
    "Aaj ka shukriya: ghar, dosti aur ek achhi chai ☕ #AajKeAcheDin"
]

# Function to authenticate and post tweet
def post_tweet(account):
    try:
        auth = tweepy.OAuth1UserHandler(
            account['consumer_key'], account['consumer_secret']
        )
        auth.set_access_token(account['access_token'], account['access_token_secret'])
        api = tweepy.API(auth)

        content = random.choice(content_list)
        api.update_status(content)
        print(f"✅ Tweet sent: {content} | From account ending in: {account['access_token'][-4:]}")
    except Exception as e:
        print(f"❌ Error tweeting from account ending in: {account['access_token'][-4:]} -> {e}")

# Schedule tweets every 10 minutes for each account
def schedule_posts():
    for account in accounts:
        schedule.every(10).minutes.do(post_tweet, account=account)

    print("📅 Scheduler started. Tweets will be posted every 10 minutes.")
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start scheduling
schedule_posts()