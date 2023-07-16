# 1.sort()、 sorted()(1)
# 函式內包含 key 和 reverse 參數 ( 可都不填 )，key 則表示進行比較的元素，reverse 不填則使用預設 False，進行升序排序 ( 小到大 )，如果參數為 True 進行降序排序 ( 大到小 )，如果排序的是字串，以字母的順序進行排序。
# sort() 函式使用後，會直接將原本的串列項目進行排序，因此「會改變」原始的串列。
a = [0,3,2,1,4,9,6,8,7,5]
a.sort()
print(a)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.sort(reverse = True)
print(a)   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# 2.sort()、 sorted()(2)
# sorted() 函式使用後，會產生一個排序過後的新串列，因此「不會改變」原始的串列。
a = [0,3,2,1,4,9,6,8,7,5]
b = sorted(a)
c = sorted(a, reverse = True)
print(a)   # [0, 3, 2, 1, 4, 9, 6, 8, 7, 5]
print(b)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(c)   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# 3.sort()、 sorted()(3)
# 如果序列的內容也是序列，排序時可以透過 key 參數，指定對應的項目進行排序。
a = [[1,2,3],[9,8,7],[2,4,6],[3,1,9]]
b = sorted(a)
c = sorted(a, key = lambda s: s[1])
print(a)   # [[1, 2, 3], [9, 8, 7], [2, 4, 6], [3, 1, 9]]
print(b)   # [[1, 2, 3], [2, 4, 6], [3, 1, 9], [9, 8, 7]] 使用第一個項目 1,2,3,9 排序
print(c)   # [[3, 1, 9], [1, 2, 3], [2, 4, 6], [9, 8, 7]] 使用第二個項目 1,2,4,8 排序


# 4.反轉串列(1)
# slice
a = [0,1,2,3,4,5]
b = a[::-1]
print(a)   # [0, 1, 2, 3, 4, 5]
print(b)   # [5, 4, 3, 2, 1, 0]


# 5.反轉串列(2)
# reverse()
a = [0,1,2,3,4,5]
a.reverse()
print(a)   # [5, 4, 3, 2, 1, 0]


# 6.複製串列(1)
# slice、copy()、list()
a = [0,1,2,3,4,5]
b = a[:]
c = a.copy()
d = list(a)
print(a)   # [0, 1, 2, 3, 4, 5]
print(b)   # [0, 1, 2, 3, 4, 5]
print(c)   # [0, 1, 2, 3, 4, 5]
print(d)   # [0, 1, 2, 3, 4, 5]


# 7.複製串列(2)
# 上述的三種方式只能針對「項目內容不會發生變化」的串列，如果項目的「深層內容」會發生變化，就會出現奇怪的現象。
a = [0,1,2,3,4,[100,200]]
b = a[:]
c = a.copy()
d = list(a)
a[-1][0] = 999
print(a)   # [0, 1, 2, 3, 4, [999, 200]]
print(b)   # [0, 1, 2, 3, 4, [999, 200]]
print(c)   # [0, 1, 2, 3, 4, [999, 200]]
print(d)   # [0, 1, 2, 3, 4, [999, 200]]


# 8.複製串列(3)
import copy
a = [0,1,2,3,4,[100,200]]
b = a[:]
c = a.copy()
d = list(a)
e = copy.deepcopy(a)
a[-1][0] = 999
print(a)   # [0, 1, 2, 3, 4, [999, 200]]
print(b)   # [0, 1, 2, 3, 4, [999, 200]]
print(c)   # [0, 1, 2, 3, 4, [999, 200]]
print(d)   # [0, 1, 2, 3, 4, [999, 200]]
print(e)   # [0, 1, 2, 3, 4, [100, 200]]  使用 deepcopy 的沒有被改變


# 9.index() 取得項目 offset
a = ["apple","banana","banana","orange"]
print(a.index('banana'))   # 1


# 10.len() 取得串列長度
a = ["apple","banana","banana","orange"]
print(len(a))   # 4


# 11.count() 計算內容出現次數
a = ["apple","banana","banana","orange"]
print(a.count("banana"))   # 2
print(a.count("grap"))     # 0


# 12.join() 結合串列內容
a = ["hello world", "I am oxxo", "how are you?"]
b = ", ".join(a)  # 使用逗號「,」進行結合
print(b)  # hello world, I am oxxo, how are you?


# 13.in 檢查內容是否存在
a = ["apple","banana","banana","orange"]
print("orange" in a)    # True
print("melon" in a)     # False


# 14.比較串列
# 使用等號「==」、「!=」，可以比較兩個串列是否相等，使用大於小於符號「<」、「<=」、「>=」、「>」，可以比較串列的長度。
# 注意，串列的比較只能針對「同樣型別」的資料，如果比較數值和字串的內容，就會發生錯誤。
a = [1,2,3,4]
b = [1,2,3,4,5]
print(a == b)     # False
print(a >= b)     # False
print(a < b)      # True
print(a != b)     # True


# 15.使用 ＊ 號重複項目
a = ["apple","banana"]
b = a * 3
print(a)   # ["apple", "banana"]
print(b)   # ["apple", "banana", "apple", "banana", "apple", "banana"]
