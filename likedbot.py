from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ========== CONFIGURATION ==========

# Bas tweet URLs yahan daal
TWEET_URLS = [
    "https://x.com/RajKumawat34981/status/1948713674988028401",
    "https://x.com/RajKumawat34981/status/1947538481451778328"
]

if __name__ == "__main__":
    # Chrome ko incognito mode me open karna
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Browser launch karna
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Twitter login page open karna
        driver.get("https://x.com/i/flow/login")
        print("🔐 Please log in manually in the browser window.")
        
        # Wait for manual login
        input("✅ Press Enter here in terminal after login is complete...")

        # Har tweet visit karke Like karna
        for tweet_url in TWEET_URLS:
            driver.get(tweet_url)
            print(f"👉 Visiting tweet: {tweet_url}")
            time.sleep(5)  # Tweet load hone ka time

            try:
                # Like button dhoondhna aur click karna
                like_button = driver.find_element(By.XPATH, '//div[@data-testid="like"]')
                like_button.click()
                print("❤️ Tweet liked.")
            except Exception as e:
                print(f"⚠️ Could not like the tweet: {e}")
            
            time.sleep(5)  # Next tweet se pehle rukna

        print("🎉 All tweets visited and (attempted) liked. Done!")

    except Exception as e:
        print(f"❌ Error occurred: {e}")

