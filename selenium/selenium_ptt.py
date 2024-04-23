# 載入相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 抓Chrome Driver檔案路徑
options = Options()
# options.executable_path = "/Users/york8536/Desktop/python/chromedriver"
options.executable_path = "/usr/local/bin/chromedriver"

# 建立Driver 物件實體，用程式操作 瀏覽器 運作
driver = webdriver.Chrome(options=options)
# 設定隱式等待時間為10秒
driver.implicitly_wait(10)
url="https://www.ptt.cc/bbs/HatePolitics/index4078.html"
driver.get(url)

# # 取得原始碼
# print(driver.page_source)

while True:
    # # 搜尋class為title的標籤
    alltitles = driver.find_elements(By.CLASS_NAME, "title")

    # 印出所有標題
    for printtitle in alltitles:
        # 印出所有標題
        print(printtitle.text)

    # 搜尋下頁按鈕的標籤
    btn= driver.find_element(By.LINK_TEXT, "下頁 ›")

    # 若按鈕class屬性="btn wide disabled"停止迴圈，否則點擊下頁
    if "btn wide disabled" in btn.get_attribute("class"):
        break
    else:
        btn.click()

# 關閉此次執行的WebDriver
driver.close()

# 屬性定位方法：
# By.ID：使用元素的 ID 屬性進行定位。
# By.NAME：使用元素的 name 屬性進行定位。
# By.CLASS_NAME：使用元素的 class 屬性進行定位。
# By.TAG_NAME：使用元素的標籤名稱進行定位。
# By.LINK_TEXT：使用元素的鏈接文本進行定位。
# By.PARTIAL_LINK_TEXT：使用元素的部分鏈接文本進行定位。
# By.CSS_SELECTOR：使用 CSS 選擇器進行定位。
# By.XPATH：使用 XPath 表達式進行定位。

# 方法定位方式：
# find_element(by, value)：定位單個元素。
# find_elements(by, value)：定位多個元素。
