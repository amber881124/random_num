# 注意:檔案名稱不能取為random.py，會發生以下錯誤
# AttributeError: partially initialized module 'random' has no attribute 'randint' (most likely due to a circular import)

import random
random_num = random.randint(1, 100)

while True:
    guess_num = input('請輸入1到100任意一個數字: ')
    guess_num = int(guess_num)
    if guess_num == random_num:
        print("你猜對了~")
        break
    elif guess_num > random_num:
        print("在小一點")
    elif guess_num < random_num:
        print("在大一點")