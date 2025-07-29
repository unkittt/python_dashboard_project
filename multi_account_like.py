from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ========== CONFIGURATION ==========

TWEET_URLS = [
    "https://x.com/abhishek3231351/status/1946474783232696757?t=VTGtXsnH-J13IG8-Ls3V_A&s=19"
]

NUM_ACCOUNTS = 5  # Kitne accounts se karna hai

def run_for_one_account(account_num):
    print(f"\n Starting automation for Account #{account_num}")

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://x.com/i/flow/login")
        print(f" [Account {account_num}] Please log in manually in the browser window.")
        input(f" [Account {account_num}] Press Enter after login...")

        for tweet_url in TWEET_URLS:
            driver.get(tweet_url)
            print(f"👉 [Account {account_num}] Visiting: {tweet_url}")
            time.sleep(5)

            try:
                like_button = driver.find_element(By.XPATH, '//div[@data-testid="like"]')
                like_button.click()
                print(f" [Account {account_num}] Tweet liked.")
            except Exception as e:
                print(f" [Account {account_num}] Could not like: {e}")

            time.sleep(5)

        print(f" [Account {account_num}] Done.")

    except Exception as e:
        print(f" [Account {account_num}] Error: {e}")

    finally:
        driver.quit()
        print(f"[Account {account_num}] Browser closed.")


if __name__ == "__main__":
    for i in range(1, NUM_ACCOUNTS + 1):
        run_for_one_account(i)
