# 1.and 和 or 的使用原則
# 使用 and 運算，如果全部都是 True，回傳最右邊 True 的值，否則回傳第一個 False 的值。
# 使用 or 運算，如果全為 False，回傳最右邊 False 的值，否則回傳第一個 True 的值。
# 元素除了 0、空 ( 空字串、空列表...等 )、None 和 False，其他在判斷式裡，全都是 True。
# 越左方 ( 越前方 ) 會越先判斷，逐步往右邊判斷。
# 除了從左向右判斷，同時使用多個 and、or 或 not，會先判斷 not，再判斷 and，最後再判斷 or。


# 2.在判斷式裡使用 and 和 or(1)
a = 1
b = 2
c = 3
if a < b and a < c:
    print("ok1")    # 顯示 ok1
if a < b or a > c:
    print("ok2")    # 顯示 ok2


# 3.在判斷式裡使用 and 和 or(2)
a = 2
b = 3
c = 0
if a > b or a < c or a == 2:
    print("ok1")       # 印出 ok1


# 4.在判斷式裡使用 and 和 or(3)
a = 2
b = 3
c = 0
if a > b or a < c or a == 2 and b == 4:    # 效果等同 (a > b or a < c) or (a == 2 and b == 4)
    print("ok1")
else:
    print("XXX")       # 印出 XXX


# 5.在判斷式裡使用 and 和 or(4)
a = 2
b = 3
c = 0
if a > b or a < c and a == 2 or b == 4:    # 效果等同 (a > b or (a < c and a == 2)) or b == 4
    print("ok1")
else:
    print("XXX")       # 印出 XXX


# 6.使用 and 和 or 回傳值(1)
a = 1 and 2 and 3
print(a)            # 3，全部都 True，所以回傳最右邊的值

b = 1 and 0 and 2
print(b)            # 0，遇到 0 ( False )，回傳第一個 False 的值就是 0

c = 1 or 2 or 3
print(c)            # 1，全部都 True，所以回傳第一個值

d = 1 or 0 or 3
print(d)            # 1，遇到 0 ( False )，回傳第一個 True 的值就是 1

e = 1 and 2 or 3
print(e)            # 2，效果等同 1 and ( 2 or 3 )

f = 1 or 2 and 3
print(f)            # 1，效果等同 1 or ( 2 and 3 )，2 和 3 先取出 3 之後變成 1 or 3

g = 1 and 2 or 3 and 4 or 5
print(g)            # 2，效果等同 1 and ( 2 or ( 3 and ( 4 or 5 )))


# 7.使用 and 和 or 回傳值(2)
a = 1
b = 2
c = 3
if(a and b and c):   # 回傳 3 --> True
    print("ok")      # 印出 ok


# 8.使用 and 和 or 回傳值(3)
a = 1
b = 0               # b 等於 0
c = 3
if(a and b and c):  # 回傳 0 --> False
    print("ok")
else:
    print("not ok")  # 印出 not ok
