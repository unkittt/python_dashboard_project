from selenium import webdriver
from seleniumwire import webdriver  

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ========== CONFIGURATION ==========

PROXY = "http://customer-shubham_tueoN-cc-in:Jaishriram_123@cnt9t1is.com:8000"

TWEET_URLS = [
    "https://x.com/RajKumawat34981/status/1948713674988028401",
    "https://x.com/RajKumawat34981/status/1947538481451778328"
]

if __name__=="__main__":
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f'--proxy-server={PROXY}')
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open Twitter login page
        driver.get("https://x.com/i/flow/login")
        print("Please log in manually in the browser window.")
        input("Press Enter here in the terminal after you have completed login...")

        for tweet_url in TWEET_URLS:
            driver.get(tweet_url)
            print(f"Navigated to tweet: {tweet_url}")
            time.sleep(5)  # Wait for tweet to load

            try:
                # Attempt to find the Like button and click it
                like_button = driver.find_element(By.XPATH, '//div[@data-testid="like"]')
                like_button.click()
                print("✅ Tweet liked.")
            except Exception as e:
                print(f"❌ Could not like the tweet: {e}")
            
            time.sleep(5)

        print("All tweets visited and liked. Exiting...")

    except Exception as e:
        print(f"An error occurred: {e}")
