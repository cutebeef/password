#密碼重試程式

#先在程式碼中 設定好密碼 password = 'a123456'
#讓使用者【最多輸入3次密碼】
#不對的話，就印出"密碼錯誤! 還有_次機會"
#對的話，就印出"登入成功!"

password = 'a123456'
i = 3
while True:
    psd = input('請輸入密碼') #不要再用password，已經被指定為正確密碼了
    if psd == password:
	    print('登入成功!')
	    break #逃出迴圈 
    else:
	    i = i - 1
	    print('密碼錯誤! 還有',i , '次機會')
	    if i == 0:
	        break
	       



#如何重複要人輸入密碼？
#要怎表達這是第幾次輸入錯誤，還剩幾次機會？
#輸入錯誤次數超過三次還是繼續，怎停止
