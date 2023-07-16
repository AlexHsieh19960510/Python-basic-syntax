# 1.建立集合(1)
# 集合由「數字、字串或布林」。
# set()
#  set() 可以建立空集合，或將串列、tuple、字串或字典轉換為集合，使用的方法為「set(要變成集合的元素)」。
a = set()
b = set([1,2,3,4,5,1,2,3,4,5])
c = set({"x":1,"y":2,"z":3})
d = set("hello")
print(a)   # set()
print(b)   # {1, 2, 3, 4, 5}  只留下不重複的部分
print(c)   # {"x", "y", "z"}  如果是字典，只保留鍵
print(d)   # {"l", "o", "h", "e"}  只留下不重複的部分


# 2.建立集合(1)
# 大括號 {}
# 如果不是空集合，可以使用「{項目}」建立集合 ( 單純寫大括號，會變成「空字典」 )。
a = {0,1,2,3,"a","b",False}
print(a)  # {0, 1, 2, 3, "a", "b"}  False 等同於 0，所以只保留 0


# 3.add() 加入項目
# 集合.add(項目)
a = {0,1,2,3,4,5}
a.add("x")
a.add("y")
print(a)   # {0, 1, 2, 3, 4, 5, "x", "y"}


# 4.移除項目(1)
# remove()
# 集合.remove(項目)
a = {0,1,2,3,"x","y","z"}
a.remove("x")
print(a)   # {0, 1, 2, 3, "y", "z"}


# 5.移除項目(2)
# discard()
# 集合.discard(項目)
a = {0,1,2,3,"x","y","z"}
a.remove("x")
a.discard("a")   # 不會發生錯誤
print(a)         # {0, 1, 2, 3, "y", "z"}


# 6.交集、聯集、差集、對稱差集(1)
# 集合	        方法	                運算子
# 交集	    a.intersection(b)	        a&b
# 聯集	    a.union(b)	                a｜b
# 差集	    a.difference(b)	            a-b
# 對稱差集	a.symmetric_difference(b)	a^b


# 7.交集、聯集、差集、對稱差集(2)
a = {1,2,3,4,5}
b = {3,4,5,6,7}

# 交集
print(a.intersection(b))   # {3, 4, 5}
print(a & b)                 # {3, 4, 5}
# 聯集
print(a.union(b))          # {1, 2, 3, 4, 5, 6, 7}
print(a | b)                 # {1, 2, 3, 4, 5, 6, 7}
# 差集
print(a.difference(b))     # {1, 2}
print(a - b)                 # {1, 2}
# 對稱差集
print(a.symmetric_difference(b))  # {1, 2, 6, 7}
print(a ^ b)                        # {1, 2, 6, 7}


# 8.子集合、超集合(1)
# 集合	        說明
# 超集合	A 完全包含 B，A 和 B 所包含的元素可能完全相同
# 真超集合	A 完全包含 B，且具有 B 沒有的的元素
# 子集合	B 完全被 A 包含，A 和 B 所包含的元素可能完全相同
# 真子集合	B 完全被 A 包含，且 A 具有 B 沒有的的元素


# 9.子集合、超集合(2)
a = {1,2,3,4,5,6,7}
b = {3,4,5,6,7}
c = {1,2,3,4,5,6,7}
d = {6,7,8,9}

print(a <= a)   # True 自己是自己的子集合
print(b <= a)   # True b 是 a 的子集合
print(b < a)    # True b 也是 a 的真子集合 ( 因爲沒有等於，完全包含 )
print(c <= a)   # True c 是 a 的子集合
print(a <= c)   # True a 也是 c 的子集合
print(d < a)    # False d 和 a 沒有子集合或超集合關係


# 10.子集合、超集合(3)
a = {1,2,3,4,5,6,7}
b = {3,4,5,6,7}
c = {1,2,3,4,5,6,7}
d = {6,7,8,9}

print(b.issubset(a))     # True b 是 a 的子集合
print(a.issuperset(b))   # True a 是 b 的超集合
print(c.issubset(a))     # True c 是 a 的子集合
print(d.issubset(a))     # Fasle d 不是 a 的子集合


# 11.len() 取得長度
a = {1,2,3,4,5,6,7}
print(len(a))   # 7


# 12.in 檢查是否存在
a = {"a","b","c","d",1,2,3}
print("b" in a)    # True
print(2 in a)      # True
print(99 in a)     # False
