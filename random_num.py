# 注意:檔案名稱不能取為random.py，會發生以下錯誤
# AttributeError: partially initialized module 'random' has no attribute 'randint' (most likely due to a circular import)

import random

start = int(input('請輸入隨機數起始: '))
end = int(input('請輸入隨機數結束: '))
random_num = random.randint(start, end)
n = 0 # 數猜了幾次
while True:
    guess_num = input(f'請輸入{start}到{end}任意一個數字: ')
    guess_num = int(guess_num)
    n += 1
    if guess_num == random_num:
        print("你猜對了~")
        break
    elif guess_num > random_num:
        print("在小一點")
    elif guess_num < random_num:
        print("在大一點")
print(f'你總共猜了{n}次')