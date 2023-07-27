# -------------------------------------------------------------------載入相關模組
from selenium import webdriver # 瀏覽器驅動工具
from selenium.webdriver.chrome.options import Options # 對瀏覽器進行設定
from selenium.webdriver.common.by import By  # 抓網頁標籤元素
from selenium.webdriver.common.keys import Keys  # 輸入文字
import datetime # 自動生成日期
import time  # 暫停
import csv # 寫入CSV檔
from selenium.common.exceptions import WebDriverException  # 捕獲處理WebDriver異常狀況


# -------------------------------------------------------------------設定Chrome Driver 的執行檔案路徑
options = Options()
options.executable_path = "/Users/york8536/Desktop/python/chromedriver"
options.add_argument("--auto-open-devtools-for-tabs")  # 開啟F12

# -------------------------------------------------------------------建立Driver 物件實體，用程式操作 瀏覽器 運作
driver = webdriver.Chrome(options=options)

# -------------------------------------------------------------------獲取當前時間
nowtime = datetime.datetime.now()

# -------------------------------------------------------------------轉換時間格式
timestamp = nowtime.strftime("%Y_%m_%d_%H_%M_%S")

# -------------------------------------------------------------------開啟網站
url="https://ubo.holy-cash.com/login"
driver.get(url)

# -------------------------------------------------------------------找到帳號密碼欄位及登入按鍵 / 輸入帳密並點擊登入
username = driver.find_element(By.ID, ":r0:")
username.send_keys("uatQAyork")
password = driver.find_element(By.ID, ":r1:")
password.send_keys("qa156156")
loginbtn = driver.find_element(By.CSS_SELECTOR,"[type='button']")
loginbtn.send_keys(Keys.ENTER)

# -------------------------------------------------------------------完成以上動作後停止X秒
time.sleep(3)

# -------------------------------------------------------------------出錯時抓consolelog並寫入csv檔案
console_logs = driver.get_log("browser")

if  console_logs != "":
    with open(f"log{timestamp}.csv", mode="w", newline="") as log:
        csv.writer(log).writerow(console_logs)

# -------------------------------------------------------------------抓到活動管理按鍵 並點擊
ActivityManagement = driver.find_element(By.XPATH, "//span[contains(text(), '活動管理')]")
ActivityManagement.click()
time.sleep(2)

# -------------------------------------------------------------------抓到活動設置按鍵 並點擊
ActivitySettings = driver.find_element(By.XPATH, "//span[contains(text(), '活動設置')]")
ActivitySettings.click()
time.sleep(2)

# -------------------------------------------------------------------截圖
driver.save_screenshot("123.png")

# -------------------------------------------------------------------關閉此次執行的WebDriver
driver.close()
