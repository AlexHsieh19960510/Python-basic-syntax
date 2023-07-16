# 1.建立字串(1)
print("hello")  # hello
print('hello')  # hello


# 2.建立字串(2)
print("'oxxo' is my name")  # 'oxxo' is my name
print('"oxxo" is my name')  # "oxxo" is my name


# 3.建立字串(3)
a = """Millions of developers and companies build,
ship, and maintain their software on GitHub—the
largest and most advanced development platform
in the world."""
print(a)


# 4.建立字串(4)
a = str(123)
print(a)   # "123"


# 5.轉義(1)
# 轉義字元	              說明
# \ ( 放在一行結尾 )	接續下一行
# \\	               顯示反斜線
# \'	               顯示單引號
# \"	               顯示雙引號
# \b	               刪除前一個字元
# \n	               換行
# \t	               tab 鍵


# 6.轉義(2)
a = 'hello "World", my name is \'oxxo\', \\_\\'
print(a)

# hello "World", my name is 'oxxo', \_\


# 7.轉義(3)
a = "hello World,\nmy name is oxxo,\nhow are you?"
print(a)

# hello World,
# my name is oxxo,
# how are you?


# 8.前方加上 r
a = r"123\n456"
b = "123\n456"
print(a)     # 123\n456
print(b)
# 123
# 456


# 9.結合字串(1)
a = "hello"
b = " world"  # 前方補上空格
c = a + b + "!!!"
print(c)

# hello world!!!


# 10.結合字串(2)
a = "hello" " world" "!!!"
print(a)

# hello world!!!


# 11.結合字串(3)
a = ("a" "b" "c" "'" "ok" "'")
print(a)

# abc'ok'


# 12.重複字串(1)
a = "ok"* 10
print(a)

# okokokokokokokokokok


# 13.重複字串(2)
a = "ok"* 5
b = a * 4
print(b)

# okokokokokokokokokokokokokokokokokokokok


# 14.取得字元與字串(1)
a = "hello world"
print(a[0])    # h ( 第一個字元 )
print(a[3])    # l ( 第四個字元 )
print(a[-1])   # d ( 最後一個字元 )


# 15.取得字元與字串(2)
# 定義	                        說明
# [ : ]	                取出全部字元，從開始到結束
# [ start: ]	        取出從 start 的位置一直到結束的字元
# [ :end ]	            取出從開始一直到 end 的「前一個位置」字元
# [ start:end ]	        取出從 start 位置到 end 的「前一個位置」字元
# [ start:end:step ]	取出從 start 位置到 end 的「前一個位置」字元，並跳過 step 個字元


# 16.取得字元與字串(3)
a = "0123456789abcdef"
print(a[:])       # 0123456789abcdef ( 取出全部字元 )
print(a[5:])      # 56789abcdef ( 從 5 開始到結束 )
print(a[:5])      # 01234 ( 從 0 開始到第 4 個 ( 5-1 ) )
print(a[5:10])    # 56789 ( 從 5 開始到第 9 個 ( 10-1 ) )
print(a[5:-3])    # 56789abc ( 從 5 開始到倒數第 4 個 ( -3-1 ) )
print(a[5:10:2])  # 579 ( 從 5 開始到第 9 個，中間略過 2 個 )


# 17.len() 取得字串長度
a = "0123456789_-\\\"\'"
print(len(a)) # 15，不包含三個反斜線 \


# 18.split() 拆分
a = "hello world, I am oxxo, how are you?"
b = a.split(",") # 以逗號「,」進行拆分
c = a.split(" ") # 以空白字元「 」進行拆分
d = a.split()    # 如果不指定分隔符號，自動以空白字元進行拆分
print(b)         # ['hello world', ' I am oxxo', ' how are you?']
print(c)         # ['hello', 'world,', 'I', 'am', 'oxxo,', 'how', 'are', 'you?']
print(d)         # ['hello', 'world,', 'I', 'am', 'oxxo,', 'how', 'are', 'you?']


# 19.replace() 替換
a = "hello world, lol"
b = a.replace("l","XXX")
c = a.replace("l","XXX",2)
print(b)  # heXXXXXXo worXXXd, XXXoXXX ( 所有的 l 都被換成 XXX )
print(c)  # heXXXXXXo world, lol ( 前兩個 l 被換成 XXX )


# 20.strip() 剝除
a = "  hello!!"
b = a.strip()
e = a.strip("!")
c = a.lstrip()
d = a.rstrip()
print(b) # hello!!
print(c) # hello!!
print(d) #   hello!!
print(e) #   hello


# 21.搜尋和選擇(1)
# 如果沒有找到結果，find() 會回報 -1 的數值，index() 會直接顯示錯誤訊息。
a = "hello world, I am oxxo, I am a designer!"
b = a.find("am")
c = a.rfind("am")
print(b)  # 15 ( 第一個 am 在 15 的位置 )
print(c)  # 26 ( 最後一個 am 在 26 的位置 )


# 22.搜尋和選擇(2)
#   函式	            說明
# startswith()	判斷開頭字串，符合 True，不符合 False
# endswith()	判斷結尾字串，符合 True，不符合 False
# isalnum()	    判斷是否只有字母和數字，符合 True，不符合 False
# count()	    計算字串出現了幾次


# 23.搜尋和選擇(3)
a = "hello world, I am oxxo, I am a designer!"
b = a.startswith("hello")
c = a.endswith("hello")
d = a.isalnum()
e = a.count("am")
print(b)   # True  ( 開頭是 hello )
print(c)   # False ( 結尾不是 hello )
print(d)   # False ( 裡面有逗號和驚嘆號 )
print(e)   # 2 ( 出現兩次 am )


# 24.大小寫(1)
#   函式	        說明
# title()	    單字字首字母變大寫
# upper()	    所有字母變大寫
# lower()	    所有字母變小寫
# swapcase()	單字字母的大小寫對調


# 25.大小寫(2)
a = "Hello world, I am OXXO"
b = a.title()
c = a.upper()
d = a.lower()
e = a.swapcase()
print(b) # Hello World, I Am Oxxo
print(c) # HELLO WORLD, I AM OXXO
print(d) # hello world, i am oxxo
print(e) # hELLO WORLD, i AM oxxo
