# -------------------------------------------------------------------載入相關模組
from selenium import webdriver # 瀏覽器驅動工具
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options # 對瀏覽器進行設定
from selenium.webdriver.common.by import By  # 抓網頁標籤元素
from selenium.webdriver.common.keys import Keys  # 輸入文字
import datetime # 自動生成日期
import time  # 暫停
import csv # 寫入CSV檔
from selenium.common.exceptions import WebDriverException  # 捕獲處理WebDriver異常狀況


# -------------------------------------------------------------------設定Chrome Driver 的執行檔案路徑
options = Options()
# Mac會有自己的預設路徑'/usr/local/bin'，直接把chromedriver放進去，若沒有預設路徑則直接使用以下方式設置
# options.chrome_executable_path = "/Users/york8536/Desktop/python/chromedriver"
options.add_argument("--auto-open-devtools-for-tabs")  # 開啟F12


# -------------------------------------------------------------------建立Driver 物件實體，用程式操作瀏覽器
driver = webdriver.Chrome(options=options)

# -------------------------------------------------------------------獲取當前時間
nowtime = datetime.datetime.now()

# -------------------------------------------------------------------轉換時間格式
timestamp = nowtime.strftime("%Y_%m_%d_%H_%M_%S")

# -------------------------------------------------------------------開啟網站
url="https://qbo.089453.fun/login"
driver.get(url)

# -------------------------------------------------------------------找到帳號密碼欄位及登入按鍵 / 輸入帳密並點擊登入
username = driver.find_element(By.ID, ":r0:")
username.send_keys("*****")
password = driver.find_element(By.ID, ":r1:")
password.send_keys("*****")
loginbtn = driver.find_element(By.CSS_SELECTOR,"[type='button']")
loginbtn.send_keys(Keys.ENTER)
time.sleep(1)

# -------------------------------------------------------------------抓到活動管理按鍵 並點擊
ActivityManagement = driver.find_element(By.XPATH, "//span[contains(text(), '活動管理')]")
ActivityManagement.click()
time.sleep(2)

# -------------------------------------------------------------------抓到活動設置按鍵 並點擊
ActivitySettings = driver.find_element(By.XPATH, "//span[contains(text(), '活動設置')]")
ActivitySettings.click()
time.sleep(2)

# -------------------------------------------------------------------抓到新增按鍵 並點擊
addActivity = driver.find_element(By.XPATH, "//button[contains(text(), '新增')]")
addActivity.click()
print(addActivity.text)
time.sleep(2)

# -------------------------------------------------------------------抓到並填寫活動名稱欄位
activityName = driver.find_element(By.XPATH, "//html/body/div[6]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div/input")
activityName.send_keys("QAtool週任務")
time.sleep(2)

# -------------------------------------------------------------------展開活動類型列表
openActivityName = driver.find_element(By.XPATH, "//html/body/div[6]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/input")
openActivityName.click()
time.sleep(0.5)

# -------------------------------------------------------------------填入活動類型
chooseActivityName = driver.find_element(By.XPATH, "//html/body/div[7]/div/ul/li[2]")
chooseActivityName.click()
time.sleep(0.5)

# -------------------------------------------------------------------填入活動時間
chooseActivityName = driver.find_element(By.CSS_SELECTOR, "div.rs-picker-toggle.rs-btn.rs-btn-default.rs-btn-lg")
chooseActivityName.click()
time.sleep(0.5)

# -------------------------------------------------------------------點擊確定
addActivityFinish = driver.find_element(By.XPATH, "//html/body/div[6]/div[3]/div/div[2]/span[1]/button")
addActivityFinish.click()
time.sleep(5)

# -------------------------------------------------------------------出錯時抓consolelog並寫入csv檔案
console_logs = driver.get_log("browser")
if  console_logs != "":
    with open(f"log{timestamp}.csv", mode="w", newline="") as log:
        csv.writer(log).writerow(console_logs)

# -------------------------------------------------------------------截圖
driver.save_screenshot("123.png")

# -------------------------------------------------------------------關閉此次執行的WebDriver
driver.close()
