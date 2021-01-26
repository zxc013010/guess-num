#產生一個1~100隨機整數，但不印出
#使用者可重複輸入數字進行猜測
#若使用者猜對 即印出 '終於猜對了!'
#若使用者猜錯 則印出 比答案大或小

import random
number = random.randint(1,100)
while True:
	guess = input("請從1~100猜一個數:")
	guess = int(guess)
	if guess == number:
		print('終於猜對了!')
		break
	else:
		if number > guess:
			print('答案比', guess, '大')
		else:
			print('答案比', guess, '小')