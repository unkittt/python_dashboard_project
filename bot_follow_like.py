from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ========== CONFIGURATION ==========

TWEET_URLS = [
    "https://x.com/abhishek3231351/status/1946474783232696757"
]

ACCOUNTS = [
    {"username": "jatnivoice", "password": "jaishriram#2028"}
    
]

def run_for_one_account(account, account_num):
    print(f"\n🔁 Starting automation for Account #{account_num}")

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://x.com/i/flow/login")
        time.sleep(5)

        # Login step
        username_input = driver.find_element(By.NAME, "text")
        username_input.send_keys(account["username"])
        driver.find_element(By.XPATH, '//div[@role="button"]').click()
        time.sleep(3)

        # Sometimes Twitter asks again
        try:
            username_input = driver.find_element(By.NAME, "text")
            username_input.send_keys(account["username"])
            driver.find_element(By.XPATH, '//div[@role="button"]').click()
            time.sleep(3)
        except:
            pass

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(account["password"])
        driver.find_element(By.XPATH, '//div[@role="button"]').click()
        time.sleep(5)

        if "login" in driver.current_url:
            print(f"❌ [Account {account_num}] Login failed.")
            return

        for tweet_url in TWEET_URLS:
            driver.get(tweet_url)
            print(f"👉 [Account {account_num}] Visiting tweet: {tweet_url}")
            time.sleep(5)

            # LIKE
            try:
                like_button = driver.find_element(By.XPATH, '//div[@data-testid="like"]')
                like_button.click()
                print(f"❤️ [Account {account_num}] Tweet liked.")
            except Exception as e:
                print(f"⚠️ [Account {account_num}] Could not like: {e}")
            time.sleep(2)

            # FOLLOW
            try:
                # Find author's profile link
                author_link = driver.find_element(By.XPATH, '//div[@data-testid="User-Names"]//a')
                profile_url = author_link.get_attribute("href")
                print(f"👤 [Account {account_num}] Going to author profile: {profile_url}")
                driver.get(profile_url)
                time.sleep(5)

                # Check if "Follow" button is visible
                follow_btn_xpath = '//div[@data-testid="placementTracking"]//span[normalize-space()="Follow"]'
                follow_button = driver.find_element(By.XPATH, follow_btn_xpath)
                follow_button.click()
                print(f"➕ [Account {account_num}] Followed the user.")
            except Exception as e:
                print(f"⚠️ [Account {account_num}] Could not follow: {e}")
            time.sleep(3)

        print(f"🎉 [Account {account_num}] Done.")

    except Exception as e:
        print(f"❌ [Account {account_num}] Error: {e}")
    finally:
        driver.quit()
        print(f"❎ [Account {account_num}] Browser closed.")


if __name__ == "__main__":
    for i, account in enumerate(ACCOUNTS, 1):
        run_for_one_account(account, i)
