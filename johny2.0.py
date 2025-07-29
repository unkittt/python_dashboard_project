import tweepy
import random
import threading

# --- Replace with your real keys and tokens ---
API_KEYS = [
    {
        "consumer_key": "Ttj4M4jHdW8Q8rnBqSRa3K8As",
        "consumer_secret": "VYjMhIxtN2T6NnP05yyFbn8GVnXIyLkyii5Dxj31TyyigC0Pwi",
        "access_token": "1946912883704467456-kmLJQI71FEpK7h0PfUP6Sg8mUtU8IH",
        "access_token_secret": "Rm7pgEGNh4UcYxYdew1gPOuTsraGn5IRQygIgW0ANKuos"
    },
    {
        "consumer_key": "hs6a0nGbjONmmr1DPKUqdUmoD",
        "consumer_secret": "ZRBc3kTfXxdv8cU8FfuqzkRiZ0lmTKMYIJtwfzAzwXc66U4izp",
        "access_token": "1946887778974769152-tB3tbcEYIrGpMGtoQw2n2bE6Z8IRev",
        "access_token_secret": "2QzCH2SNRqyftzChqTNhKLEmlPPKBBI9czAGVQRsJOqc9"
    },
    {
        "consumer_key": "mP8D4IVaacoN3iqFbKRBEk6HF",
        "consumer_secret": "BEONpeA6ZBu4DXt6RXWEAGAS7fghOnNnJd4KvfYZcUjoZ2gvSM",
        "access_token": "1946893057393111040-3cXXr13zR9KdcAIC6Te2B6gNR6cBBY",
        "access_token_secret": "MlJrgLgJGiVhAjslwmkEPwLH0BOkOLiyuh7zsO77VAwSF"
    },
    {
        "consumer_key": "bkgbPcBaHgnEn1Nh9Baajbbec",
        "consumer_secret": "jtnVPpF671sJABzLZZ68Ihbvmg0AoY6ebuNklsHLePbnOMAFoJ",
        "access_token": "1946895801348956160-vq5djsCgy0tIoATdwoTXlLedXVLKwH",
        "access_token_secret": "ivlU48SgyUXONW13jlLN9gPgiuObH0BRoCeLiP9ykBDOu"
    },
    {
        "consumer_key": "z1Ea1myoVe0f5WoJQBMKvdNFB",
        "consumer_secret": "SGfcPcaw3qlvNgJoBgO8RnGKWvVoM8q4cANF8ebAtGR6BbRDk5",
        "access_token": "1946898457303941120-vlgpbVJq3nM36NjGYojR4VnqqOJGI9",
        "access_token_secret": "8WhW7AE1ObeRBwMgpBzzqm1QrpA5gK2VsNV8cGX6BGoRa"
    }
]

# --- Original tweet content per bot ---
content_list = [
    "Bot 1 tweeting something cool! #Tweet1",
    "Bot 2 sending good vibes. #Tweet2",
    "Bot 3 has joined the chat. #Tweet3",
    "Bot 4 is live now. #Tweet4",
    "Bot 5 making a move. #Tweet5"
]

# --- Random rephrasing ---
def rephrase_content(text):
    rephrased = [
        f"{text} - Just a spin!",
        f"Here’s a rephrased: {text}",
        f"Alternate version: {text}",
        f"{text} (fresh take!)"
    ]
    return random.choice(rephrased)

# --- Decide original or rephrased ---
def get_random_content(original):
    return original if random.choice([True, False]) else rephrase_content(original)

# --- Tweepy v2 Client using OAuth1.0a Tokens ---
def create_client(credentials):
    return tweepy.Client(
        consumer_key=credentials["consumer_key"],
        consumer_secret=credentials["consumer_secret"],
        access_token=credentials["access_token"],
        access_token_secret=credentials["access_token_secret"],
        wait_on_rate_limit=True
    )

# --- Bot tweet function ---
def post_tweet(index, client, content):
    try:
        tweet_text = get_random_content(content)
        response = client.create_tweet(text=tweet_text)
        print(f"✅ Bot {index + 1} Tweeted: {tweet_text}")
    except Exception as e:
        print(f"❌ Bot {index + 1} failed: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    threads = []

    for i in range(len(API_KEYS)):
        client = create_client(API_KEYS[i])
        thread = threading.Thread(target=post_tweet, args=(i, client, content_list[i]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("🚀 All bots finished tweeting.")
