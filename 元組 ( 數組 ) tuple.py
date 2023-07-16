# 1.tuple 與串列 list 的差異
# tuple「只要建立了，就不能修改內容」。
# tuple 使用「小括號」，串列 list 使用「方括號」。
# 如果 tuple 裡只有一個元素，後方必須加上「逗號」( 多個元素就不用 )。


# 2.使用 tuple 的好處
# 讀取速度比串列快。
# 佔用的空間比較少。
# 資料更安全 ( 因為無法修改 )。


# 3.建立 tuple(1)
# 使用小括號和逗號
# 注意，因為 b 只有一個元素，所以元素後方要加上逗號 。
a = ("apple","banana","orange","grap")
b = ("apple",)
type(a)  # tuple
type(b)  # tuple


# 4.建立 tuple(2)
# 使用 tuple()
a = ["apple","banana","orange","grap"]
b = tuple(a)
type(b)  # tuple


# 5.讀取 tuple 的內容(1)
# 使用變數
t = ("apple","banana","orange","grap")
a, b, c, d = t
print(a)   # apple
print(b)   # banana
print(c)   # orange
print(d)   # grap


# 6.讀取 tuple 的內容(2)
# 索引值 offset
t = ("apple","banana","orange","grap")
print(t[0])   # apple
print(t[1])   # banana
print(t[2])   # orange
print(t[3])   # grap


# 7.使用 + 號結合 tuple
t1 = ("apple","banana","orange")
t2 = ("grap","pineapple")
t = t1 + t2
print(t)   # ("apple", "banana", "orange", "grap", "pineapple")


# 8.使用＊號重複項目
a = ("apple","banana","orange")
b = a * 3
print(b)   # ("apple", "banana", "orange", "apple", "banana", "orange", "apple", "banana", "orange")


# 9.強制修改 tuple
a = ("apple","banana","orange")
b = list(a)
b.append("grap")
a = tuple(b)
print(a)   # ("apple", "banana", "orange", "grap")