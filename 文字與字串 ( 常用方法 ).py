# 1.str(x)
# 將 x 轉換成字串的型態。
a = str(123)
print(a)   # 123 ( 字串型態，不是數字 )


# 2.+ 結合字串
# 將不同的字串結合在一起。
a = "abc"
b = "123"
print(a + b)   # abc123


# 3.＊ 重複字串
# 將同一個字串重複指定的次數。
a = "abc"
print(a * 3)


# 4.str[]
# 取出字串中的某些字元。
a = "0123456789abcdef"
print(a[0])       # 0 ( 第一個字元 )
print(a[3])       # 3 ( 第四個字元 )
print(a[-1])      # f ( 最後一個字元 )
print(a[:])       # 0123456789abcdef ( 取出全部字元 )
print(a[5:])      # 56789abcdef ( 從 5 開始到結束 )
print(a[:5])      # 01234 ( 從 0 開始到第 4 個 ( 5-1 ) )
print(a[5:10])    # 56789 ( 從 5 開始到第 9 個 ( 10-1 ) )
print(a[5:-3])    # 56789abc ( 從 5 開始到倒數第 4 個 ( -3-1 ) )
print(a[5:10:2])  # 579 ( 從 5 開始到第 9 個，中間略過 2 個 )


# 5.len(str)
# 取得字串長度 ( 有幾個字元 )。
a = "hello world"
print(len(a))    # 11


# 6.str.split(x)
# 根據 x 字元拆分字串，使字串變成串列形式。
a = "hello world, I am oxxo, how are you?"
b = a.split(",") # 以逗號「,」進行拆分
c = a.split(" ") # 以空白字元「 」進行拆分
d = a.split()    # 如果不指定分隔符號，自動以空白字元進行拆分
print(b)         # ['hello world', ' I am oxxo', ' how are you?']
print(c)         # ['hello', 'world,', 'I', 'am', 'oxxo,', 'how', 'are', 'you?']
print(d)         # ['hello', 'world,', 'I', 'am', 'oxxo,', 'how', 'are', 'you?']


# 7.str.join(iter)
# 將原本的字串，結合指定的序列，變成新的字串。
a = ["hello world", "I am oxxo", "how are you?"]
b = ", ".join(a)  # 使用逗號「,」進行結合
print(b)  # hello world, I am oxxo, how are you?


# 8.str.replace(x, y, n)
# 將字串中的 x 替換為 y，n 為要替換的數量，可不填 ( 表示全部替換 )。
a = "hello world, lol"
b = a.replace("l","XXX")
c = a.replace("l","XXX",2)
print(b)  # heXXXXXXo worXXXd, XXXoXXX ( 所有的 l 都被換成 XXX )
print(c)  # heXXXXXXo world, lol ( 前兩個 l 被換成 XXX )


# 9.str.strip()(1)
# 去除字串開頭或結尾的某些字元。
a = "  hello!!"
b = a.strip()
c = a.strip("!")
d = a.lstrip()
e = a.rstrip()
print(b) # hello!!
print(c) #   hello
print(d) # hello!!    使用 lstrip() 函式可以只去除左邊
print(e) #   hello!!  使用 rstrip() 函式可以只去除右邊


# 10.str.strip()(2)
s = "@!$##$#ABCDE%#$#%#$"
a = s.strip("!@#$%^&*(")
print(a)  # ABCDE


# 11.str.capitalize()
# 將字串的字首變成大寫。
a = "hello world, i am oxxo!"
b = a.capitalize()
print(b)    # Hello world, i am oxxo!


# 12.str.casefold()、str.lower()
# 將字串全部轉成小寫，str.casefold() 更會將一些其他語系的小寫字母作轉換。
a = "Hello World, I am OXXO!"
b = a.casefold()
c = a.lower()
print(b)    # hello world, i am oxxo!
print(c)    # hello world, i am oxxo!


# 13.str.upper() 
# 將字串全部轉成大寫。
a = "Hello World, I am OXXO!"
b = a.upper()
print(b)    # HELLO WORLD, I AM OXXO!


# 14.str.title()
# 將字串全部轉成標題 ( 每個單字字首大寫 )。
a = "Hello world, I am OXXO! How are you?"
b = a.title()
print(b)    # Hello World, I Am Oxxo! How Are You?


# 15.str.swapcase()
# 將字串的大小寫對調。
a = "Hello World, I am OXXO!"
b = a.swapcase()
print(b)   # hELLO WORLD, i AM oxxo!


# 16.str.count(sub, start, end)
# 計算某段文字在字串中出現的次數 ( start、end 為範圍，可不填 )。
a = "Hello World, I am OXXO!"
b = a.count("o")
c = a.count("o", 1, 5)
print(b)     # 2
print(c)     # 1


# 17.str.index(sub, start, end)
# 尋找某段文字在字串中出現的位置 ( start、end 為範圍，可不填 )。
a = "Hello World, I am OXXO!"
b = a.index("w")
print(b)     # 6


# 18.str.encode(encoding='utf-8', errors='strict')
# 針對字串進行編碼。
a = "Hello world, 喔哈！"
b = a.encode(encoding = "utf-8", errors = "strict")
c = a.encode(encoding = "BIG5", errors = "strict")
print(b)    # b'Hello world, \xe5\x96\x94\xe5\x93\x88\xef\xbc\x81'
print(c)    # b'Hello world, \xb3\xe1\xab\xa2\xa1I'


# 19.sub in str
# 判斷字串中是否存在某段文字，回傳 True 或 False ( 也可使用 not in 判斷是否不存在 )。
a = "Hello world!"
print("wo" in a)      # True
print("ok" not in a)  # True


# 20.str.isalnum()
# 判斷字串中是否都是英文字母或數字 ( 不能包含空白或符號 )，回傳 True 或 False。
a = "Helloworld123"
b = "Helloworld123!!"
c = "Hello world"
print(a.isalnum())   # True
print(b.isalnum())   # False ( 包含驚嘆號 )
print(c.isalnum())   # False ( 包含空白 )


# 21.str.isalpha()
# 判斷字串中是否都是英文字母 ( 不能包含數字、空白或符號 )，回傳 True 或 False。
a = "Helloworld"
b = "Helloworld123"
c = "Hello world"
print(a.isalpha())   # True
print(b.isalpha())   # False ( 包含數字 )
print(c.isalpha())   # Fasle ( 包含空白 )


# 22.str.isdigit()
# 判斷字串中是否都是數字 ( 不能包含英文、空白或符號 )，回傳 True 或 False。
a = "12345"
b = "Hello123"
c = "1 2 3"
print(a.isdigit())   # True
print(b.isdigit())   # False  ( 包含英文 )
print(c.isdigit())   # Fasle  ( 包含空白 )


# 23.str.islower()
# 判斷字串中是否都是小寫英文字母 ( 忽略數字和符號 )，回傳 True 或 False。
a = "hello world 123"
b = "Hello World 123"
print(a.islower())    # True
print(b.islower())    # False ( H 和 W 是大寫 )


# 24.str.isupper()
# 判斷字串中是否都是大寫英文字母 ( 忽略數字和符號 )，回傳 True 或 False。
a = "HELLO 123"
b = "Hello 123"
print(a.isupper())    # True
print(b.isupper())    # False


# 25.str.istitle()
# 判斷字串中是否為標題 ( 每個單字字首大寫 )，回傳 True 或 False。
a = "Hello World I Am Oxxo 123!!"
b = "Hello World I Am OXXO 123!!"
c = "Hello world, I am OXXO 123!!"
print(a.istitle())    # True
print(b.istitle())    # False ( OXXO 全都大寫 )
print(c.istitle())    # False ( world 和 am 字首沒有大寫 )