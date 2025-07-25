import tweepy
import os

# --- Apni Twitter API credentials yahan daalo ---
API_KEY = 'iWtS9iHZco2Scm8oyPEGwV71B'
API_SECRET = '04Ij3rUUtlMGksVWe9JSqb4Te5Jwuu6nAp7ZBtKqaoajoobH8d'
ACCESS_TOKEN = '1945041474569060352-NeRAzBEyvAK06UGQy0IYA41yEhubWV'
ACCESS_TOKEN_SECRET = 'EOoT0qRqeoThz4KBuFYzD9GI4bsdlR1P0GqIVdqlAGyFV'

# Tweepy v1.1 API (for media upload)
auth_v1 = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api_v1 = tweepy.API(auth_v1)

# Tweepy v2 Client (for tweeting)
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

def reply_with_image(tweet_url, reply_text, image_path):
    tweet_id = extract_tweet_id(tweet_url)
    if not tweet_id:
        print("❌ Cannot reply: Invalid tweet URL or tweet ID not found.")
        return

    if not os.path.isfile(image_path):
        print(f"❌ Image file not found: {image_path}")
        return

    try:
        # Upload media with v1.1 API
        media = api_v1.media_upload(image_path)
        media_id = media.media_id_string

        # Reply with media_id attached
        response = client.create_tweet(
            text=reply_text,
            in_reply_to_tweet_id=tweet_id,
            media_ids=[media_id]
        )
        print(f"✅ Successfully replied with image to tweet ID {tweet_id}")
    except Exception as e:
        print("❌ Error replying with image:", e)

if __name__ == "__main__":
    tweet_link = "https://x.com/TikaRamJullyINC/status/1948335947591893085"
    reply_message = "बात जब रोजगार की होती है तो टिकराम जूली जाति की चौखट तोड़ने के बजाय उसे और मजबूत करते हैं।#टीकाराम_जूली_जातिवादी_कीड़ा."

    # Image path - change this to your image file path
    image_file_path = "C:/Users/Admin/Desktop/poster123.jpg"  # Example: "C:/Users/Admin/Desktop/poster.jpg"

    reply_with_image(tweet_link, reply_message, image_file_path)
