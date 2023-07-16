# 1.建立串列(1)
# 中括號 ( 方括號 )
a = ["apple","banana","orange"]
b = [1,2,3,4,5]
c = ["apple",1,2,3,["dog","cat"]]
print(type(a))   # <class 'list'>
print(type(b))   # <class 'list'>
print(type(c))   # <class 'list'>


# 2.建立串列(2)
# list()
a = ("apple","banana","orange")
b = list(a)
c = list()
d = list("apple")
print(b)   # ['apple', 'banana', 'orange']
print(c)   # []
print(d)   # ['a', 'p', 'p', 'l', 'e']


# 3.建立串列(3)
# split() + 字串
a = "apple...banana...orange"
b = a.split(".")
print(b)   # ["apple", "", "", "banana", "", "", "orange"]


# 4.合併串列(1)
# 使用 + 號
a = ["a1","a2","a3"]
b = ["b1","b2","b3"]
c = a + b
print(c)   # ["a1","a2","a3","b1","b2","b3"]


# 5.合併串列(2)
# extend()
a = ["a1","a2","a3"]
b = ["b1","b2","b3"]
a.extend(b)
print(a)   # ["a1","a2","a3","b1","b2","b3"]


# 6.合併串列(3)
a = ["a1","a2","a3"]
b = ["b1","b2","b3"]
c = a.extend(b)
print(c)   # none


# 7.讀取串列項目(1)
# offset
a = ["apple","banana","orange"]
print(a[0])   # apple
print(a[1])   # banana
print(a[2])   # orange


# 8.讀取串列項目(2)
a = ["apple","banana","orange"]
print(a[-1])   # orange
print(a[-2])   # banana
print(a[-3])   # apple


# 9.讀取串列項目(3)
a = ["apple","banana","orange",["dog","cat"]]
print(a[3][0])   # dog
print(a[3][1])   # cat


# 10.讀取串列項目(4)
# slice()
# 範圍也可以使用「負數」，表示從右側數來，但要注意第一個值的順序 ( 不論正負 ) 都必須要在第二個值的前面，不然就讀取不到項目 ( 會回傳空的結果 )。
a = [0,1,2,3,4,5,6,7,8,9]
b = a[:3]
c = a[3:]
d = a[1:3]
e = a[-5:-2]
print(b)   # [0, 1, 2]  取得 0～(3-1) 項
print(c)   # [3, 4, 5, 6, 7, 8, 9]  取得 3～最後一項
print(d)   # [1, 2]  取得 1～(3-1) 項
print(e)   # [5, 6, 7]  取得倒數第 5 項～(倒數第二項-1)


# 11.讀取串列項目(5)
a = [0,1,2,3,4,5,6,7,8,9]
b = a[::3]
c = a[3::2]
d = a[::-1]
e = a[::-2]
print(b)   # [0, 3, 6, 9]  每隔三項目取值
print(c)   # [3, 5, 7, 9]  從第三個項目開始，每隔兩項目取值
print(d)   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  反轉串列
print(e)   # [9, 7, 5, 3, 1]  反轉串列，每隔兩個項目取值


# 12.複製串列
# 串列[:]
a = [1, 2, 3]
b = a
del(a[1])    # 刪除 a 的第二個項目
print(a)     # [1, 3]
print(b)     # [1, 3]

c = [1, 2, 3]
d = c[:]     # 複製 c 的所有項目變成一個新串列
del(c[1])    # 刪除 c 的第二個項目
print(c)     # [1, 3]
print(d)     # [1, 2, 3]


# 13.修改串列項目(1)
# offset
a = ["apple","banana","orange"]
a[0] = "grap"
print(a)   # ["grap","banana","orange"]


# 14.修改串列項目(2)
# slice()
a = ["a","b","c","d","e"]
a[1:4] = [100,200,300]
print(a)    # ["a", 100, 200, 300, "e"]


# 15.修改串列項目(3)
a = ["a","b","c","d","e"]
a[1:4] = [1,2,3,4,5,6,7,8,9]
print(a)   # ["a", 1, 2, 3, 4, 5, 6, 7, 8, 9, "e"]


# 16.修改串列項目(4)
a = ["a","b","c","d","e"]
a[1:4] = "hello"
print(a)    # ["a", "h", "e", "l", "l", "o", "e']


# 17.添加串列項目(1)
# append()
a = ["a","b","c","d","e"]
a.append(100)
b = ["a","b","c","d","e"]
b.append([100,200,300])
print(a)   # ["a","b","c","d","e", 100]
print(b)   # ["a","b","c","d","e", [100, 200, 300]]


# 18.添加串列項目(2)
# insert()
a = ["a","b","c","d","e"]
a.insert(3,100)
b = ["a","b","c","d","e"]
b.insert(0,100)
c = ["a","b","c","d","e"]
c.insert(100,100)
d = ["a","b","c","d","e"]
d.insert(-1,100)
print(a)   # ["a", "b", "c", 100, "d", "e"]
print(b)   # [100, "a", "b", "c", "d", "e"]
print(c)   # ["a", "b", "c", "d", "e", 100]
print(d)   # ["a", "b", "c", "d", 100, "e"]


# 19.刪除串列項目(1)
# del
a = [0,1,2,3,4,5,6,7,8,9]
del a[2]
b = [0,1,2,3,4,5,6,7,8,9]
del b[2:6]
print(a)   # [0, 1, 3, 4, 5, 6, 7, 8, 9]
print(b)   # [0, 1, 6, 7, 8, 9]


# 20.刪除串列項目(2)
# remove()
a = ["apple","apple","banana","orange"]
a.remove("apple")
print(a)   # ["apple", "banana", "orange"]


# 21.刪除串列項目(3)
# pop()
a = [0,1,2,3,4,5]
b = a.pop(2)
print(a)   # [0, 1, 3, 4, 5]
print(b)   # 2


# 22.刪除串列項目(4)
# clear()
a = [0,1,2,3,4,5]
a.clear()
print(a)   # []