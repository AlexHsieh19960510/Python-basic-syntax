# 1.print(*objects, sep, end, file, flush)(1)
# 參數	        說明
# *objects	要印出的對象，可以用逗號分隔多個對象
# sep	    預設為「一個空白」，表示每個分隔的對象，在印出時中間的間隔符號
# end	    預設換行符「\n」，表示印出的結尾符號
# file	    預設「None」，表示要寫入的文件對象
# flush	    預設「False」，設定為 True 可以防止函式對輸出資料進行緩衝，並強行重新整理


# 2.print(*objects, sep, end, file, flush)(2)
print(1,2,3)           # 1 2 3
print(1,2,3,sep=";")   # 1;2;3
print(1,2,3,sep=";",end="!")
print(1,2,3)           # 1;2;3!1 2 3


# 3.print(*objects, sep, end, file, flush)(3)
import time
print("Loading",end = "")
for i in range(6):
    print(".",end = "",flush = True)
    time.sleep(0.5)


# 4.print(*objects, sep, end, file, flush)(4)
import time
n = 10
for i in range(n+1):
    print(f"\r倒數 {n-i} 秒", end="")
    time.sleep(1)
print("\r時間到", end="")


# 5.input(x)(1)
a = input("輸入文字：")
print("你輸入的是："+a)


# 6.input(x)(2)
a = int(input("輸入第一個數字："))
b = int(input("輸入第二個數字："))
print(f"兩個數字相加結果是：{a+b}")


# 7.input(x)(3)
import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(f"兩個數字相加結果是：{a+b}")

