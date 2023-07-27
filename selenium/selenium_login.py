# 載入相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# 設定Chrome Driver 的執行檔案路徑
options = Options()
options.executable_path = "/Users/york8536/Desktop/python/chromedriver"

# 建立Driver 物件實體，用程式操作 瀏覽器 運作
driver = webdriver.Chrome(options=options)

# 指定存取網址
url="https://qbo.089453.fun/login"
driver.get(url)

# 找到帳號密碼欄位及登入按鍵
username = driver.find_element(By.ID, ":r0:")
password = driver.find_element(By.ID, ":r1:")
loginbtn = driver.find_element(By.CSS_SELECTOR,"[type='button']")

# 輸入帳密並點擊登入
username.send_keys("york0001")
password.send_keys("qa156156")
loginbtn.send_keys(Keys.ENTER)

# 完成以上動作後停止X秒
time.sleep(5)



# 關閉此次執行的WebDriver
# driver.close()
