import tweepy

# Twitter API credentials for multiple accounts
accounts = [
    {
        'consumer_key': 'goDyLjhdSy5ZlZDcGJbcxio3A',
        'consumer_secret': 'JuMiRjHxUJm8HBGiduRFZCw4TlMkPiwCNzA9xoLSaP4E5ySDQx',
        'access_token': '1945449057285193728-mOPRKqSUm1vKLAyBB8lDBAoO5P7LFR',
        'access_token_secret': '1NyIyvhVnLm4VXXZauWloQuQP0B5lOOAv8VpQfBvLGA4y'
    },
    {
        'consumer_key': 'DEfBq2m0tSf2FKOEQJDBDCN79',
        'consumer_secret': 'amvv8cl6GTASQvYKc2AEY8LcJpmppxsZMOYmDxHLl7t78lN499',
        'access_token': '1941084288134324224-D3BkDVWlwNpUH72KWWg5Mn08Z3z5EK',
        'access_token_secret': 'qXIivnAlVHyQ5OwYF7ff6UdLAM5wDAXMme9Dwn7RjcKbf'
    },
    {
        'consumer_key': 'KkASO8IS15TRNWnRS4bxlHXyy',
        'consumer_secret': 'vUP4GfyWSLRPfUlywa2jtBdHVdplK0M0HXNHt8BLOXWIvlHXyD',
        'access_token': '1945448277589237760-rLdVdUPXX6yIwjPX8YSdhFGeV0leRA',
        'access_token_secret': 'cb5yA4XNmMqQWGU5VcZaYBqmuzbPctbNmpMf6lusaVy0u'
    },
    {
        'consumer_key': 'pZJCOWWwLLaEncRR3jaur1Wc7',
        'consumer_secret': 'haFDYrNhYRqvzGpkvElLSp9QStYIgcaLXQL01RYIWG5Gn9v3oE',
        'access_token': '1943921637847642112-ODV0lmYJyMh79aadSkYMD6Res1Ngj7',
        'access_token_secret': 'aUAtH3hFDuqLb2GHedJQ9lQjKKwc2Trke4GvA5iTEGgKi'
    }
    # Add more accounts as needed
]

# Function to authenticate and create API object for each account
def authenticate_and_create_api(account):
    auth = tweepy.OAuthHandler(account['consumer_key'], account['consumer_secret'])
    auth.set_access_token(account['access_token'], account['access_token_secret'])
    api = tweepy.API(auth)
    return api

# Main execution
if __name__ == "__main__":
    api_objects = []
    for account in accounts:
        try:
            api = authenticate_and_create_api(account)
            api_objects.append(api)
            print("Authenticated successfully for account:", account['consumer_key'])
        except Exception as e:
            print(f"Failed to authenticate {account['consumer_key']}: {e}")

    # Now you can use the api_objects list to interact with Twitter via multiple accounts