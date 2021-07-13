car = input('請問你有沒有開車：')
age = input('請輸入你的年齡：')
age = int(age)
if car == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼開過車')
elif car == '沒有':
	if age >= 18:
		print('你可以考駕照了啊')
	else:
		print('乖寶寶！繼續保持')