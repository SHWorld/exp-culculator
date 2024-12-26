import math
base = 10000  # 基本経験値
n = int(input("正解数を入力: "))  # 正解数
s = int(input("不正解数を入力: "))  # 不正解数
l = n + s  # 総問題数
t = int(input("セット連続数を入力: "))  # セットの連続成功数

correct = 1 + 0.005 * n
false  = 1 + 0.02 * s
questions =1 + 0.005 * l

consecutibeofnumbers = (1.1 + 0.9 / (1 + math.e**(-0.35*(t - 10)))) 
# 経験値計算
result = base * correct * false * questions * consecutibeofnumbers
print(result)