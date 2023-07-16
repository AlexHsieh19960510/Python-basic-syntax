# 1.if 判斷
a = 2
b = 3
if a > b:
    print("hello")  # 不會印出，因為結果為 False
print("ok")       # ok


# 2.if、else
a = 2
b = 3
if a > b:
    print("hello")    # 不會印出，因為結果為 False
else:
    print("world")    # world
print("ok")           # ok


# 3.if、elif、else(1)
# 一個邏輯判斷裡，只會有一個 if 和 else，但可以有多個 elif。
# 不論是 if、elif 還是 else，最後只會有一種結果。
a = 2
b = 3
if a > b:
    print("a > b")    # 不會印出
elif a<b:
    print("a < b")    # a<b
else:
    print("a = b")    # 不會印出
print("ok")         # ok


# 4.if、elif、else(2)
a = 2
b = 3
if a > b:
    pass            # 不做任何動作
elif a < b:
    print("a > b")    # a<b
else:
    print("a = b")    # 不會印出
print("ok")         # ok


# 5.巢狀判斷
a = 2
b = 3
if a < b:
    print("a < b")      # a<b
    if a == 1:
        print("a = 1")  # 不會印出
    elif a == 2:
        print("a = 2")  # a=2
    elif a == 3:
        print("a = 3")  # 不會印出
elif a > b:
    print("a > b")      # 不會印出
else:
    print("a = b")      # 不會印出
print("ok")           # ok


# 6.三元運算式 ( 條件運算式 )(1)
# 變數 = 值1 if 條件式 else 值2
a = 1
b = 2
c = ""
if a > b:
    c = "a"
else:
    c = "b"
print(c)    # b


# 7.三元運算式 ( 條件運算式 )(2)
a = 1
b = 2
c = ""
c = "a" if a > b else "b"
print(c)     # b
