from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["Name or Number"])

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

print("🔓 QR code scan कर और group manually खोल")
input("✅ Group खुलने के बाद Enter दबा")

time.sleep(5)

for i in range(5):
    driver.execute_script("document.querySelector('[data-testid=\"chat-info-drawer\"]')?.scrollBy(0, 300)")
    time.sleep(1)

members = driver.find_elements(By.XPATH, '//div[@role="button"]//span[@dir="auto"]')
unique_names = set()

for member in members:
    name = member.text.strip()
    if name and name not in unique_names:
        sheet.append([name])
        unique_names.add(name)

wb.save("group_members.xlsx")
print("✅ Excel file 'group_members.xlsx' बन गई")
driver.quit()