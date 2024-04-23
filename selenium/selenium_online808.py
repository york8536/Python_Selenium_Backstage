# 載入相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# 設定Chrome Driver 的執行檔案路徑
options = Options()
# options.executable_path = "/Users/york8536/Desktop/python/chromedriver"

# 建立Driver 物件實體，用程式操作 瀏覽器 運作
driver = webdriver.Chrome(options=options)
# 設定隱式等待時間為10秒
driver.implicitly_wait(10)
# 指定存取網址
url="https://leetcode.com/accounts/login/"
driver.get(url)
time.sleep(50)
# -------------------------------------------------------------------抓到已滿18歲按鍵 並點擊
btn18 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div[2]/div/div/div/button")
btn18.click()

time.sleep(1)

# # -------------------------------------------------------------------抓到登入按鍵 並點擊
# login = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[2]/div[2]/div/div[2]/div/img")
# login.click()

# time.sleep(3)

# # -------------------------------------------------------------------抓到記住我的帳號 並點擊
# # login = driver.find_element(By.XPATH, "/html/body/div[34]/div/div/div[2]/div/div/form/div[4]/div/div[1]/label/input")
# # login.click()

# # time.sleep(3)

# # -------------------------------------------------------------------抓到我不是機器人 並移動滑鼠至上方 並點擊
# notrobot = driver.find_element(By.XPATH, "/html/body/div[34]/div/div/div[2]/div/div/form/div[4]/div/div[2]/div/div/iframe")
# actions = ActionChains(driver)
# actions.move_to_element(notrobot).pause(3)

# notrobot.click()

time.sleep(3)





