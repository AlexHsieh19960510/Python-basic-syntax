# 1.list(x)
# list(x) 可以建立空串列，或將「字串、tuple、字典或集合」轉變成串列 。
a = "12345"
b = (1,2,3,4,5)
c = {1,2,3,4,5,"x","y","z"}
d = {"x":"1","y":"2","z":"3"}
print(list(a))    # ["1", "2", "3", "4", "5"]
print(list(b))    # [1, 2, 3, 4, 5]
print(list(c))    # [1, 2, 3, 4, 5, "z", "y", "x"]
print(list(d))    # ["x", "y", "z"]


# 2.dict(x) 
# dict(x) 可以建立空字典，或將「帶有鍵與值、兩個值的二維串列或 tuple、雙字元的字串串列或 tuple」轉變成字典 。
a = dict(name = "oxxo", age = 18, eat = ["apple","banana"])
b = dict([["x","100"],["y","200"],["z","300"]])
c = dict(["ab","cd","ef"])
print(a)    # {"name": "oxxo", "age": 18, "eat": ["apple", "banana"]}
print(b)    # {"x": "100", "y": "200", "z": "300"}
print(c)    # {"a": "b", "c": "d", "e": "f"}


# 3.set(x)
# set(x) 可以建立空集合，或將「串列、tuple、字串或字典」轉換為集合。
a = set()
b = set([1,2,3,4,5,1,2,3,4,5])
c = set({"x":1,"y":2,"z":3})
d = set("hello")
print(a)   # set()
print(b)   # {1, 2, 3, 4, 5}  只留下不重複的部分
print(c)   # {"x", "y", "z"}  如果是字典，只保留鍵
print(d)   # {"l", "o", "h", "e"}  只留下不重複的部分


# 4.frozenset(x)
# frozenset(x) 可以建立一個「不可改變」的集合。
a = frozenset()
b = frozenset([1,2,3,4,5,1,2,3,4,5])
c = frozenset({"x":1,"y":2,"z":3})
d = frozenset("hello")
print(a)   # frozenset()
print(b)   # frozenset({1, 2, 3, 4, 5})
print(c)   # frozenset({"x", "z", "y"})
print(d)   # frozenset({"e", "h", "l", "o"})


# 5.tuple(x)
# tuple(x) 可以建立空 tuple，或將「串列、集合、字串或字典」轉換為集合。
a = tuple([1,2,3,4,5])
b = tuple("12345")
c = tuple({"1","2","3","4","5"})
d = tuple({"x":"1","y":"2","z":"3"})
print(a)    # (1, 2, 3, 4, 5)
print(b)    # ("1", "2", "3", "4", "5")
print(c)    # ("4", "2", "3", "1", "5")
print(d)    # ("x", "y", "z")


# 6.enumerate(x, start=y)
# enumerate() 可以將「串列、集合、tuple、字典」建立為可迭代並附加索引值的 enumerate 物件，start 的數值代表索引值開始的數字，預設從 0 開始 ( 不填入預設 0 )。
a = enumerate(["a","b","c"])
b = enumerate(("a","b","c"))
c = enumerate({"a","b","c"})
d = enumerate({"a":1,"b":2,"c":3}, start = 2)
print(a)          # <enumerate object at 0x7f8de8677050>
print(list(a))    # [(0, "a"), (1, "b"), (2, "c")]
print(list(b))    # [(0, "a"), (1, "b"), (2, "c")]
print(list(c))    # [(0, "a"), (1, "b"), (2, "c")]
print(list(d))    # [(2, "a"), (3, "b"), (4, "c")] 設定 start=2，第一項的索引值變成 2


# 7.iter(x)
# iter() 可以將「串列、集合、tuple、字典」建立為可迭代的 iter 物件。
a = iter([1,2,3])
b = iter((1,2,3))
c = iter({"a","b","c"})
d = iter({"a":1,"b":2,"c":3})
print(a)    # <list_iterator object at 0x7f8de866e450>
print(b)    # <tuple_iterator object at 0x7f8de866ec90>
print(c)    # <set_iterator object at 0x7f8de86c0910>
print(d)    # <dict_keyiterator object at 0x7f8de86ec7d0>


# 8.next(x)
# next() 通常和 iter() 與 enumerate() 搭配，可以將 enumerate 和 iter 物件的內容「依序取出並移除」，每執行一次就取出一個，直到完全取出為止。
a = enumerate(["a","b","c"])
print(next(a))    # (0, "a")
print(next(a))    # (1, "b")
print(next(a))    # (2, "c")
print(list(a))    # []    # 全部取出後只剩下空串列

b = iter(["a","b","c"])
print(next(b))    # a
print(next(b))    # b
print(next(b))    # c
print(list(b))    # []    # 全部取出後只剩下空串列
