height = float(input('請輸入身高：'))
weight = float(input('請輸入體重：'))

if height > 100:
	height /= 100

bmi = weight / (height * height)

if bmi < 18.5:
	print('您的BMI為：', bmi,'->過輕')
elif bmi >= 18.5 and bmi < 24:
	print('您的BMI為：', bmi,'->正常')
elif bmi >= 24 and bmi < 27:
	print('您的BMI為：', bmi,'->過重')
elif bmi >= 27 and bmi < 30:
	print('您的BMI為：', bmi,'->輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('您的BMI為：', bmi,'->中度肥胖')
else:
	print('您的BMI為：', bmi,'->重度肥胖')