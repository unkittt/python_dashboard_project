import tweepy

# --- Apni Twitter API credentials yahan daalo ---
API_KEY = 'iWtS9iHZco2Scm8oyPEGwV71B'
API_SECRET = '04Ij3rUUtlMGksVWe9JSqb4Te5Jwuu6nAp7ZBtKqaoajoobH8d'
ACCESS_TOKEN = '1945041474569060352-NeRAzBEyvAK06UGQy0IYA41yEhubWV'
ACCESS_TOKEN_SECRET = 'EOoT0qRqeoThz4KBuFYzD9GI4bsdlR1P0GqIVdqlAGyFV'


# Tweepy client setup
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)

def extract_tweet_id(tweet_url):
    try:
        status_index = tweet_url.find("status/")
        if status_index == -1:
            raise ValueError("Invalid tweet URL: 'status/' not found")

        after_status = tweet_url[status_index + len("status/"):]
        tweet_id = ''
        for ch in after_status:
            if ch.isdigit():
                tweet_id += ch
            else:
                break

        if not tweet_id:
            raise ValueError("No tweet ID digits found")

        return tweet_id
    except Exception as e:
        print("Error extracting tweet ID:", e)
        return None

def reply_to_tweet(tweet_url, reply_text):
    tweet_id = extract_tweet_id(tweet_url)
    if not tweet_id:
        print("❌ Cannot reply: Invalid tweet URL or tweet ID not found.")
        return

    try:
        response = client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet_id)
        print(f"✅ Successfully replied to tweet ID {tweet_id}")
    except Exception as e:
        print("❌ Error replying:", e)

if __name__ == "__main__":
    tweet_link = "https://x.com/TikaRamJullyINC/status/1948335947591893085"
    reply_message = "हर बार सीएम को घेरते हैं जाति के नाम पर, काम पे सवाल करने का साहस कहां?#टीकाराम_जूली_जातिवादी_कीड़ा."
    reply_to_tweet(tweet_link, reply_message)
