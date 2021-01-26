#猜數字遊戲 設定規則如下:
#讓使用者產生一區間範圍整數
#使用者所產生之區間範圍若非合理範圍，需讓使用者產生至合理範圍為止
#使用者可重複猜測遊戲數字，直至答對為止
#在使用者猜出正確數字時 即印出 '恭喜您! 第__次終於猜對了! 答案是__'
#在使用未猜到正確數字時 則印出 比答案大或小
#使用者在未猜出答案前 需印出 '這是您猜的第__次'

import random
start = input('請輸入遊戲開始值 (須為整數):')
end = input('請輸入遊戲結束值 (須為整數):')
start = int(start)
end = int(end)
while True:
	if start < end:
		number = random.randint(start,end)
		count = 0
		while True:
			count += 1
			guess = input('請從範圍內猜一個數:')
			guess = int(guess)
			if guess == number:
				print('恭喜您! 第', count, '次終於猜對了!', '答案是', number)
				break
			else:
				if number > guess:
					print('答案比', guess, '大')
				else:
					print('答案比', guess, '小')
			print('這是您猜的第', count, '次')
		break	
	else:
		print("遊戲開始值須小於遊戲結束值")
		start = input('請輸入遊戲開始值:')
		end = input('請輸入遊戲結束值:')
		start = int(start)
		end = int(end)		