# 1.int(x, base)(1)
a = int("123")
b = int(123.999)
c = int()
d = int(True)
e = int(False)
print(a)    # 123
print(b)    # 123
print(c)    # 0
print(d)    # 1
print(e)    # 0


# 2.int(x, base)(2)
a = int("123")
b = int("123", base = 8)
c = int("123", base = 16)
print(a)    # 123
print(b)    # 83    123 等於 83 的八進位
print(c)    # 291   123 等於 291 的十六進位


# 3.float(x)(1)
a = float("123")
b = float(123)
c = float()
d = int(True)
e = int(False)
print(a)    # 123.0
print(b)    # 123.0
print(c)    # 0.0
print(d)    # 1.0
print(e)    # 0.0


# 4.float(x)(2)
a = float("inf")
b = float("-inf")
c = float("nan")
print(a)   # inf 正無窮大
print(b)   # -inf 負無窮大
print(c)   # nan 正無窮大


# 5.abs(x)
a = abs(-123)
print(a)   # 123


# 6.divmod(x, y)
# ( x//y, x%y ) 的 tuple。
a = divmod(5,3)
b = divmod(9,2)
print(a)   # (1, 2)
print(b)   # (4, 1)


# 7.max(iter)
a = max("100200300")
b = max([100,200,300])
c = max((100,200,300))
print(a)   # 3 ( 因為字串拆開後只有 0 1 2 3 )
print(b)   # 300
print(c)   # 300


# 8.min(iter)
a = min("100200300")
b = min([100,200,300])
c = min((100,200,300))
print(a)   # 0 ( 因為字串拆開後只有 0 1 2 3 )
print(b)   # 100
print(c)   # 100


# 9.pow(x, y, z)
# pow(x, y) 會回傳「x 的 y 次方」。
# pow(x, y, z) 會回傳「x 的 y 次方除以 z 的餘數」。
a = pow(2, 3)
b = pow(2, 3, 3)
print(a)    # 8 ( 2 的 3 次方 )
print(b)    # 2 ( 8 除以 3 的餘數 )


# 10.round(x, y)(1)
# 四捨五入後的 x，y 表示四捨五入的小數點位數。
a = round(3.14159)
b = round(3.14159, 3)
print(a)    # 3
print(b)    # 3.142


# 11.round(x, y)(2)
# 當遇到 .5 的數值時容易出現問題，因為 .5 的數字其實是 .44444444X 或 .5000000X 之類的數字，這時使用 round() 會發生預期外的狀況。
print(round(1.5))   # 2
print(round(2.5))   # 2 ( 因為 2.5 不是真正的 2.5 )
print(round(3.5))   # 4
print(round(4.5))   # 4 ( 因為 4.5 不是真正的 4.5 )
print(round(5.5))   # 6


# 12.sum(iter, y)
# 串列或 tuple 的數值與 y 的加總，如果不指定 y 則 y 為 0。
a = sum([1,2,3,4])
b = sum((1,2,3,4))
c = sum((1,2,3,4), 5)
print(a)    # 10
print(b)    # 10
print(c)    # 15  ( 最後再加上 5 )


# 13.complex(x, y)
# x + yj。
# 如果 x 是數字，需要加上數字 y，如果 x 是字串，則不需要 y。
a = complex(1, 2)
print(a)   # (1+2j)


# 14.bool(x)
# 參數 x 轉變成布林值 False 或 True
a = bool(1)
b = bool(0)
c = bool()
d = bool(999)
e = bool("hello")
f = bool([0])
g = bool([])
print(a)    # True
print(b)    # False
print(c)    # False
print(d)    # True
print(e)    # True
print(f)    # True  ( 因為串列有值 )
print(g)    # False  ( 因為串列也為空 )
