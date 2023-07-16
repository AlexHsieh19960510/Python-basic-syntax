# 1.建立字典(1)
# 大括號 {}
# 使用方式為「{'鍵':值}」，鍵必須是「字串」，前後必須加上「引號」，值則可以是任意的 Python 物件 ( 字串、數字、串列、字典...等 )，不同鍵值中間使用逗號「,」分隔。
a = {"name":"oxxo","age":18,"eat":["apple","banana"]}
print(type(a));    # <class 'dict'>


# 2.建立字典(2)
a = {}
print(type(a));   # <class 'dict'>


# 3.建立字典(3)
# dict()
# dict(鍵=值)
a = dict(name = "oxxo", age = 18, eat = ["apple","banana"])
print(a)          # {"name": "oxxo", "age": 18, "eat": ["apple", "banana"]}
print(type(a));   # <class 'dict'>


# 4.建立字典(4)
# 將有「兩個值的二維串列或 tuple」轉換成字典，轉換時會將第一個值當作鍵，第二個當成值。
a = [["x","100"],["y","200"],["z","300"]]
b = dict(a)
print(b)    # {"x": "100", "y": "200", "z": "300"}


# 5.建立字典(5)
# 將有「雙字元的字串串列」轉換成字典，轉換時會將第一個值當作鍵，第二個當成值。
a = ["ab","cd","ef"]
b = dict(a)
print(b)    # {"a": "b", "c": "d", "e": "f"}


# 6.讀取字典(1)
# 中括號 []
# 字典["鍵"]
a = {"name":"oxxo","age":18,"eat":["apple","banana"]}
b = a["name"]
c = a["eat"][0]
print(b)   # oxxo
print(c)   # apple


# 7.讀取字典(2)
# get()
# get("鍵")
a = {"name":"oxxo","age":18,"eat":["apple","banana"]}
b = a.get("name")
c = a.get("school")
print(b)   # oxxo
print(c)   # None


# 8.修改字典(1)
# 中括號 []
# 字典["鍵"]=新值
a = {"name":"oxxo","age":18}
a["name"] = "XXXX"
a["age"] = 100
print(a)   # {"name": "XXXX", "age": 100}


# 9.修改字典(2)
a = {"name":"oxxo","age":18}
a["name"] = "XXXX"
a["age"] = 100
a["ok"] = True
print(a) # {"name": "XXXX", "age": 100, "ok": True}


# 10.修改字典(3)
# setdefault()
# setdefault() 函式用法和 get() 類似，都是可以取出某個鍵的值，但如果字典中沒有對應的鍵，執行 setdefault() 就會將新的鍵和值加入字典中。
# setdefault("鍵",值)
a = {"name":"oxxo","age":18}
b = a.setdefault("age", 100)
c = a.setdefault("ok", True)
print(a)   # {"name": "XXXX", "age": 100, "ok": True}
print(b)   # 18
print(c)   # True


# 11.刪除字典(1)
# del
# del 字典["鍵"]
# del 字典
a = {"name":"oxxo","age":18}
del a["name"]
print(a)   # {"age": 18}

b = {"name":"oxxo","age":18}
del b
print(b)   # name "b" is not defined


# 12.刪除字典(2)
# pop()
# pop("鍵")
# 注意，有別於串列的 pop() 可為空，字典的 pop("鍵") 操作一定要有鍵，不然會發生錯誤 。
a = {"name":"oxxo","age":18}
b = a.pop("name")
print(a)   # {"age": 18}
print(b)   # oxxo


# 13.刪除字典(3)
# clear()
# 字典.clear()
a = {"name":"oxxo","age":18}
a.clear()
print(a)   # {}


# 14.結合字典(1)
# 兩個星號＊＊
# {**字典}
a = {"name":"oxxo","age":18}
b = {"weight":60,"height":170}
c = {"ok":True}
d = {**a, **b, **c}
print(d)   # {"name": "oxxo", "age": 18, "weight": 60, "height": 170, "ok": True}


# 15.結合字典(2)
# update()
# 字典1.update(字典2)
a = {"name":"oxxo","age":18}
b = {"weight":60,"height":170}
c = {"ok":True}
a.update(b)
a.update(c)
print(a)   # {"name": "oxxo", "age": 18, "weight": 60, "height": 170, "ok": True}


# 16.取得所有鍵和值
# 透過「字典.keys()」能夠將所有的鍵取出變成「dict_keys()」，透過「字典.values()」能夠將所有的值取出變成「dict_values()」，兩者都可以透過串列或 tuple 的方法，轉換成串列或 tuple。
a = {"name":"oxxo","age":18,"weight":60,"height":170}
b = a.keys()
c = a.values()
print(b)         # dict_keys(["name", "age", "weight", "height"])
print(c)         # dict_values(["oxxo", 18, 60, 170])
print(list(b))   # ["name", "age", "weight", "height"]
print(list(c))   # ["oxxo", 18, 60, 170]


# 17.使用 in 檢查鍵
# 鍵 in 字典
a = {"apple":10, "banana":20, "orange":30}
print("apple" in a)   # True
print("grap" in a)    # False


# 18.複製字典(1)
# copy()
# 字典.copy()
a = {"x":10, "y":20, "z":30}
b = a.copy()
print(b)   # {"x": 10, "y": 20, "z": 30}


# 19.複製字典(2)
# deepcopy()
# copy() 的方法只能針對「項目內容不會發生變化」的字典，如果字典的「深層內容」會發生變化，就會出現奇怪的現象
a = {"x":10, "y":20, "z":[100,200,300]}
b = a.copy()
a["z"][0] = 999
print(a)   # {"x": 10, "y": 20, "z": [999, 200, 300]}
print(b)   # {"x": 10, "y": 20, "z": [999, 200, 300]}


# 20.複製字典(3)
import copy
a = {"x":10, "y":20, "z":[100,200,300]}
b = copy.deepcopy(a)
a['z'][0] = 999
print(a)   # {"x": 10, "y": 20, "z": [999, 200, 300]}
print(b)   # {"x": 10, "y": 20, "z": [100, 200, 300]} 使用 deepcopy 的沒有被改變