from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ========== CONFIGURATION ==========

TWEET_URLS = [
    "https://x.com/abhishek3231351/status/1946474783232696757"
]


def run_manual_login_flow():
    print("\n🔁 Starting automation with manual login")

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Open login page
        driver.get("https://x.com/i/flow/login")
        print("🔐 Please login manually in the opened browser window.")
        input("✅ Press Enter after you have logged in successfully...")

        for tweet_url in TWEET_URLS:
            driver.get(tweet_url)
            print(f"👉 Visiting tweet: {tweet_url}")
            time.sleep(5)

            # LIKE
            try:
                like_button = driver.find_element(By.XPATH, '//div[@data-testid="like"]')
                like_button.click()
                print("❤️ Tweet liked.")
            except Exception as e:
                print(f"⚠️ Could not like tweet: {e}")
            time.sleep(2)

            # FOLLOW
            try:
                author_link = driver.find_element(By.XPATH, '//div[@data-testid="User-Names"]//a')
                profile_url = author_link.get_attribute("href")
                print(f"👤 Going to profile: {profile_url}")
                driver.get(profile_url)
                time.sleep(5)

                follow_btn_xpath = '//div[@data-testid="placementTracking"]//span[normalize-space()="Follow"]'
                follow_button = driver.find_element(By.XPATH, follow_btn_xpath)
                follow_button.click()
                print("➕ Followed the user.")
            except Exception as e:
                print(f"⚠️ Could not follow user: {e}")
            time.sleep(3)

        print("🎉 Done.")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        driver.quit()
        print("❎ Browser closed.")


if __name__ == "__main__":
    run_manual_login_flow()
