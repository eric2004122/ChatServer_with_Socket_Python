# 提示使用者輸入身高和體重
height = float(input("請輸入您的身高（公尺）："))
weight = float(input("請輸入您的體重（公斤）："))

# 計算 BMI
bmi = weight / (height ** 2)
 
# 輸出 BMI 值
print(f"您的 BMI 值為：{bmi:.2f}")

# 根據 BMI 值給出健康建議
if bmi < 18.5:
    print("體重過輕")
elif 18.5 <= bmi < 24.9:
    print("體重正常")
elif 25 <= bmi < 29.9:
    print("體重過重")
else:
    print("肥胖")