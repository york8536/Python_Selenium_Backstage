# 載入相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


# 設定Chrome Driver 的執行檔案路徑
options = Options()
options.executable_path = "/Users/york8536/Desktop/python/chromedriver"

# 建立Driver 物件實體，用程式操作 瀏覽器 運作
driver = webdriver.Chrome(options=options)


# 指定存取網址
url="https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0"
driver.get(url)

# 連續捲動迴圈
n=0
while n<3:
    n=n+1
    # 捲動視窗並載入更多內容
    # windows.scrollTo() : js滾動功能()中應填入座標，document.body.scrollHeight=底部
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    # 等待X秒
    time.sleep(3)

# 抓到列表所有title並印出
alltitles = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for printtitle in alltitles:
    print(printtitle.text)



# 關閉此次執行的WebDriver
driver.close()