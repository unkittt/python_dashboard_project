import tweepy
import time
import itertools

# ---------------------------------------
# 🔐 STEP 1: Add your API credentials here
API_KEY = 'iWtS9iHZco2Scm8oyPEGwV71B'
API_SECRET = '04Ij3rUUtlMGksVWe9JSqb4Te5Jwuu6nAp7ZBtKqaoajoobH8d'
ACCESS_TOKEN = '1945041474569060352-NeRAzBEyvAK06UGQy0IYA41yEhubWV'
ACCESS_TOKEN_SECRET = 'EOoT0qRqeoThz4KBuFYzD9GI4bsdlR1P0GqIVdqlAGyFV'
# ---------------------------------------

# Auth for v2 API (text-only tweet)
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)

# 📝 Tweets to send
tweets = [
    "Every step forward, no matter how small, is still progress. Keep climbing.",
    "Even in the toughest places, you can rise. Strength grows in silence.",
    "Believe in the power you don't see yet. Your future self is watching.",
    "The journey may be long, but the destination is worth every mile.",
    "Dreams aren’t just made in sleep — they’re built with discipline."
]

# ⏰ 15-minute loop
start_time = time.time()
end_time = start_time + 15 * 60  # 15 minutes

for tweet_text in itertools.cycle(tweets):
    if time.time() >= end_time:
        print("✅ 15 minutes completed. Tweeting stopped.")
        break

    try:
        response = client.create_tweet(text=tweet_text)
        print(f"✅ Tweeted: \"{tweet_text}\" →", response.data)
    except Exception as e:
        print("❌ Error:", e)

    time.sleep(60)  # ⏳ Wait 1 minute
