import tweepy
import time
import random

# --- Apni Twitter API credentials yahan daalo ---
API_KEYS = [
    ('cWpeL5nD2omKgJdo9Ntuf7sSA', 'cCjHbGnWC0p3e0R4jqqz5I5BV4T8XLOIlOXo71PePWGaZFviXg', '1946885239676284928-sKyqNuMXebmTUc9YyaUGWDEDYHpkGA', 'ueQQo1DxBrSv8yQ6XxWPquzennF00IFdNOHUO0UZ4AKOD'),
    ('ZBg1UP3g1bv7Vh3I2bkYP5ZCv', 'fEHQVMwYl3EEuIPiRW9ucDMnRKvcE9nCX3PGtz0JwZ50XLESZu', '1946892154577760257-hsPA0YGzoriW3VGXM14dl8Eay6F9SC', 'rsEKA5N4lNjMfs1RF2rCzVJu1APxoNysDhWRhThIjBrzY'),
    ('xZZLgz7R6APl1O97H3MKu8hps', 'l4OchsK2laY3e5IbEBR4LER4I6p2VLTcDK4i1uTWwUaFVOsjjd', '1946900256395866113-O5qFXbjZcNzvpzA8CbVkEcjRqzhVQy', 'VGXTujLWVWCyjs5M5nwNrXCiHNIkFtVXW2iFCOUHe0uL3'),
    ('evNH2cbIdTp6MQu2htmxWjzpz', 'QCUP6IVEUcCIQszHXKNUoWMqMeYSLzqkCwjtE6jV0A9WAuzJMh', '1946903181767684096-CXeTyoJcpLx37YsbjD57le1YeAfEZ8', 'gIjnP6tXewN1zftBnaCEQ2lxTYsDUsFdDY7nrbAYC1KL2'),
    ('8Il9pqlcaXg8pwUHgh0IFlYfY', '1Ba3b2erCJCiD6MfFaZiwwOQ2ipu0dgxZHj94vt8JVJIMHYEBL', '1946905075986665472-86bsTfdvttnNdJ3pL54pB46ZrArcUL', 'BofKL74xyZ90zE5fFNKvdM4petx4vsT5q2EoEhnZlAdRf')
]

# Tweepy client setup for each bot
def create_client(api_key, api_secret, access_token, access_token_secret):
    return tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True
    )

clients = [create_client(*keys) for keys in API_KEYS]

# List of original content provided by you
content_list = [
    "",
    "Here’s a different message. #RandomPost2",
    "Another tweet with different wording. #RandomPost3",
    "Here is some unique content. #RandomPost4",
    "This is the last tweet. #RandomPost5"
]

# Function to rephrase the content
def rephrase_content(original_content):
    # List of possible rephrased versions of the content (could be dynamic as well)
    rephrased_list = [
        original_content + " - Just another take on it.",
        "Here is a reworded version: " + original_content,
        "This content could also be said as: " + original_content,
        "An alternative way of saying it: " + original_content,
        original_content + " - A fresh perspective!"
    ]
    return random.choice(rephrased_list)  # Choose a random rephrased version

# Function to randomly choose between original or rephrased content
def get_random_content(original_content):
    if random.choice([True, False]):  # Randomly choose to either use the original or rephrased content
        return original_content
    else:
        return rephrase_content(original_content)

def post_tweet(post_text, bot_index):
    try:
        response = clients[bot_index].create_tweet(text=post_text)
        print(f"Successfully posted tweet using Bot {bot_index + 1}: {post_text}")
    except Exceptiong as e:
        print(f" Error posting using Bot {bot_index + 1}: {e}")

if __name__ == "__main__":
    # Loop through each bot and post a random tweet (original or rephrased)
    for i in range(5):
        original_content = content_list[i]  # Get the original content
        final_content = get_random_content(original_content)  # Get either original or rephrased content
        post_tweet(final_content, i)  # Post the chosen content
        time.sleep(5)  # Adding delay of 5 seconds between posts to avoid hitting rate limits