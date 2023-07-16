# 1.range(start, stop, step)(1)
# 產生一個「整數序列」，產生後可透過 list()、tuple() 之類的方法轉換成對應的類別。
# 參數	      說明
# start	    起始數字
# stop	   結束數字 - 1
# step	可不填，數字間隔，預設 1


# 2.range(start, stop, step)(2)
a = range(1,5)
b = range(1,100,10)
c = range(5,-5,-1)
print(list(a))   # [1, 2, 3, 4]
print(list(b))   # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
print(list(c))   # [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]


# 3.range(start, stop, step)(3)
for i in range(1,10,2):
  print(i)   # 1 3 5 7 9


# 4.len(iter)
# len(x) 可以取得串列、字典、集合、tuple 的長度 ( 有幾個項目 )，也可以取得字串的長度 ( 有幾個字母或數字 )。
a = [1,2,3,4,5]
b = (1,2,3,4,5)
c = {"x","y","z"}
d = {"a":1,"b":2,"c":3,"d":4}
e = "apple"
print(len(a))    # 5
print(len(b))    # 5
print(len(c))    # 3
print(len(d))    # 4
print(len(e))    # 5


# 5.map(function, iter)(1)
# map() 可以使用指定的函式，依序處理可迭代物件的每個項目，處理後產生一個全新的物件。
# map() 會將第二個參數的可迭代物件，提供給第一個參數的函式作為引數使用。
def a(x):
    return x + 1
b = map(a, [1,2,3,4,5])
c = map(lambda x: x + 1, [1,2,3,4,5])

print(list(b))    # [2, 3, 4, 5, 6]
print(tuple(c))   # (2, 3, 4, 5, 6)


# 6.map(function, iter)(2)
a = ["1", "2", "3" ,"4", "5"]
print(a)                # ["1", "2", "3" ,"4", "5"]

b = list(map(int, a))   # 取出 a 的每個項目，套用 int(項目)，組成新物件
print(b)                # [1, 2, 3, 4, 5]


# 7.map(function, iter)(3)
t = ["12", "34"]
a, b = map(int, t)
print(a)    # 12
print(b)    # 34


# 8.filter(function, iter)
# filter() 可以使用指定的函式，依序判斷可迭代物件的每個項目，將判斷結果為 Ture 的物件集合成為一個全新的物件。
def a(x):
  return x > 2
b = filter(a, [1,2,3,4,5])
c = filter(lambda x: x > 2, [1,2,3,4,5])

print(list(b))    # [3, 4, 5]
print(tuple(c))   # (3, 4, 5)


# 9.sorted(x, key=None, reverse=False)(1)
# sorted 可以將可迭代物件進行排序，並產生一個全新的物件。
# 參數	            說明
# x	        可迭代的物件，例如串列、字串、tuple、字典、集合
# key	    可不填，預設由第一個項目判斷 ( 如果有多層內容 )，也可指定判斷的項目
# reverse	可不填，預設 False 由小到大，設定 True 表示由大到小


# 10.sorted(x, key=None, reverse=False)(2)
a = [1,5,3,4,2]
b = sorted(a)
c = sorted(a, reverse = True)

print(list(b))   # [1, 2, 3, 4, 5]
print(list(c))   # [5, 4, 3, 2, 1]


# 11.sorted(x, key=None, reverse=False)(3)
a = [[1,8],[2,1],[5,2],[3,5],[9,3]]
b = sorted(a, key = lambda x: x[1])

def test(x):
  return x[1]

c = sorted(a, key = test)

print(list(b))   # [[2, 1], [5, 2], [9, 3], [3, 5], [1, 8]]
print(list(c))   # [[2, 1], [5, 2], [9, 3], [3, 5], [1, 8]]


# 12.reversed(x)
# reversed() 可以將有順序性的物件 ( 字串、串列和 tuple ) 內容反轉，產生一個全新的物件。
a = [1,2,3,4,5]
b = (1,2,3,4,5)
c = "12345"

print(list(reversed(a)))   # [5, 4, 3, 2, 1]
print(list(reversed(b)))   # [5, 4, 3, 2, 1]
print(list(reversed(c)))   # ["5", "4", "3", "2", "1"]


# 13.all(x)
# all() 可以判斷一個可迭代物件裡，是否包含了 False 相關的元素 ( 只要是 0、空白、False 都屬於 False 元素 )，如果包含就會回傳 False，反之不包含就會回傳 True，此外，如果是「空」的物件，會回傳 True。
a = [1,2,3,4,5]
b = [0,1,2,3,4,5]
c = ["x","y","z",""]
d = []

print(all(a))    # True
print(all(b))    # False
print(all(c))    # False
print(all(d))    # True


# 14.any(x)
# any() 可以判斷一個可迭代物件裡，是否包含了 True 相關的元素 ( 只要不是 0、空白、False 都屬於 True 元素 )，如果包含就會回傳 True，反之不包含就會回傳 False，此外，如果是「空」的物件，會回傳 False。
a = [1,2,3,4,5]
b = [0,1,2,3,4,5]
c = ["x","y","z",""]
d = []

print(any(a))    # True
print(any(b))    # True
print(any(c))    # True
print(any(d))    # False


# 15.slice(start, stop, step)(1)
# slice(start, stop, step) 可以「定義切片範圍」，當指定的可迭代物件套用範圍後，就會取出範圍內的項目，變成新的物件。
# 參數	說明
# start	起始數字
# stop	結束數字 - 1
# step	可不填，數字間隔，預設 1


# 16.slice(start, stop, step)(2)
a = slice(2,6)
b = slice(2,6,2)
c = [1,2,3,4,5,6,7,8,9]

d = c[a]
e = c[b]
print(d)      # [3, 4, 5, 6]
print(e)      # [3, 5]


# 17.zip()
# zip() 可以將指定的可迭代物件，打包變成一個新的物件，新物件的長度與「最短」的一致。
a = [1,2,3,4]
b = [5,6,7]
c = [8,9]
d = zip(a, b, c)
print(list(d))    # [(1, 5, 8), (2, 6, 9)]
