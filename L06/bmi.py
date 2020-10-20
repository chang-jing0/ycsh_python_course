a=float(input("請輸入身高（公分)"))
b=float(input("請輸入體重（公斤)"))
a=a/100
print("BMI:"+ str(round((b/(a*a)),2)))

