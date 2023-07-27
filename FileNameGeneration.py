import datetime

# 獲取當前時間
time = datetime.datetime.now()

# 轉換時間格式
timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")


# 生成文件名
file_name = f"{timestamp}.xlsx"

print(timestamp)