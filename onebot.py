import tweepy
import time
import random
from datetime import datetime
import os

# =============== ENTER YOUR API KEYS ===============
consumer_key = 'i1WhWnmDo8NrJKFAsXXiJOrku'
consumer_secret = 'CvmEPjfWc7bMgtUIxnmyfCTLNaallRo89wIVa7JWiuaISfGNmB'
access_token = '1941084288134324224-whClLHoHcodvLeZukpMNuQ2Ij15LN9'
access_token_secret = 'vAd8yZ6PArFJWs0mMGSjxv0Avu8JYrswa51PSGHfQQWrz'
hashtag = "#aajkeachedin"
# ====================================================

tweets = [
    "Zindagi choti nahi hoti, log jeena bhool jaate hain.",
    "Jo hota hai ache ke liye hota hai.",
    "Kal ki chinta mat karo, aaj pe dhyan do.",
    "Har din ek nayi shuruaat hai.",
    "Khud pe bharosa rakho, sab sahi hoga.",
    "Sapne wahi sach hote hain jinhe hum poora karne ki koshish karte hain.",
    "Muskurate raho, duniya confuse rahegi.",
    "Jo tumhe rokta hai, wahi tumhe majboot banata hai.",
    "Asli jeet wahi hai jo khud se ho.",
    "Mehnat itni karo ki taqdeer ko bhi kehna pade — lo, le bhai success!"
]

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def log(msg):
    with open("log.txt", "a", encoding='utf-8') as f:
        f.write(f"{datetime.now()} - {msg}\n")

if not os.path.exists("start.txt"):
    with open("start.txt", "w") as f:
        f.write("OFF")

print("Bot is ready.")
print("To START tweeting: write 'ON' in start.txt")
print("To STOP tweeting: write 'OFF' in start.txt\n")

while True:
    try:
        with open("start.txt", "r") as f:
            status = f.read().strip().upper()

        if status == "ON":
            message = random.choice(tweets)
            tweet_text = message + "\n" + hashtag

            try:
                api.update_status(tweet_text)
                log(f"Tweeted: {tweet_text}")
                print(f"Tweeted:\n{tweet_text}\n")
            except Exception as e:
                log(f"Error: {e}")
                print(f"Error: {e}")

            delay = random.randint(600, 1200)
            print(f"Waiting {delay // 60} minutes...\n")
            time.sleep(delay)

        else:
            print("Bot is OFF. Waiting 30 seconds...\n")
            time.sleep(30)

    except Exception as e:
        print(f"Error in loop: {e}")
        time.sleep(30)
        