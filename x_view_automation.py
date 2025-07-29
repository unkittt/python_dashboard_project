

from selenium import webdriver
from seleniumwire import webdriver  

from selenium.webdriver.chrome.options import Options
import time

# ========== CONFIGURATION ==========

# Replace with your proxy (format: ip:port, optionally with scheme: http://ip:port)
PROXY = "http://customer-shubham_tueoN-cc-in:Jaishriram_123@cnt9t1is.com:8000"

# Replace with your tweet URL
TWEET_URLS = ["https://x.com/RajKumawat34981/status/1948713674988028401", "https://x.com/RajKumawat34981/status/1947538481451778328" ]

if __name__=="__main__":
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f'--proxy-server={PROXY}')
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the Twitter login page
        driver.get("https://x.com/i/flow/login")
        print("Please log in manually in the browser window.")
        
        # Wait until user confirms they finished logging in
        input("Press Enter here in the terminal after you have completed login...")
        for tweet_url in TWEET_URLS:
            driver.get(tweet_url)
            print(f"Navigated to tweet: {tweet_url}")
            # Wait for 5 seconds before moving to the next tweet
            time.sleep(5)
        print("All the links have been viewed. Exiting...")
      
    except Exception as e:
        print(f"An error occurred: {e}")
