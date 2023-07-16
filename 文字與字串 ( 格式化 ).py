# 1.%(1)
# 格式化字串 % 資料
# 格式化字串	 轉換型態
#   %s	        字串
#   %d	        十進制整數
#   %x	        十六進制整數
#   %o	        八進制整數
#   %b	        二進制整數
#   %f	        十進制浮點數
#   %e	        指數浮點數
#   %g	        十進制或指數浮點數
#   %%	        常值 %


# 2.%(2)
a = "Hello world, I am %s!!"
b = "there are %d dollars"
c = "there are %f dollars"
print(a % "oxxo")  # Hello world, I am oxxo!!
print(a % "xoox")  # Hello world, I am xoox!!
print(b % 2.5)     # there are 2 dollars ( 小數點被無條件捨去 )
print(c % 2)       # there are 2.000000 dollars ( 整數轉換成浮點數 )


# 3.%(3)
# 格式化數值	    說明
# 不加東西、+	 靠右對齊
#   -	        靠左對齊
# 數字	         最小寬度 ( 如果字串超過最小寬度，以字串的寬度為主 )
# 數字.數字	     最小寬度.最大字元數，如果後方是 f (%f)，第二個數字表示小數點位數


# 4.%(4)
print("%s world" % "hello")      # hello world
print("%12s world" % "hello")    #        hello world
print("%+12s world" % "hello")   #        hello world
print("%-12s world" % "hello")   # hello        world
print("%.3s world" % "hello")    # hel world
print("%12.3s world" % "hello")  #          hel world
print("%.3f world" % 123.456789) # 123.457 world


# 5.%(5)
a = "%s world, ther are %f dollars!"
b = a % ("hello", 2.5)
print(b)   # hello world, ther are 2.500000 dollars!


# 6..format(1)
a = "hello {}, I am {}"
b = a.format("world", "oxxo")
print(b)   # hello world, I am oxxo


# 7..format(2)
a = "hello {1}, I am {0}"
b = a.format("world", "oxxo")
print(b)   # hello oxxo, I am world ( world 和 oxxo 互換了 )


# 8..format(3)
a = "hello {m}, I am {n}"
b = a.format(m = "world", n = "oxxo")
print(b)   # hello world, I am oxxo


# 9..format(4)
a = "hello {0[x][m]}, I am {0[y][m]}"
b = {"x": {"m":"world", "n":"oxxo"}, "y":{"m":"QQ", "n":"YY"}}
c = a.format(b)
print(c)    # hello world, I am QQ


# 10..format(5)
# 格式化數值	    說明
#   :	        開始需要加上冒號
# 不加東西、>	 靠右對齊
#   <	        靠左對齊
#   ^	        置中對齊
# 填補字元	    將不足最小寬度的空白，填滿指定字元
# 數字.數字	    最小寬度.最大字元數，如果後方是 f (%f)，第二個數字表示小數點位數

# 格式化字串     轉換型態
#   :s	        字串
#   :d	        十進制整數
#   :x	        十六進制整數
#   :o	        八進制整數
#   :b	        二進制整數
#   :f	        十進制浮點數
#   :e	        指數浮點數
#   :g	        十進制或指數浮點數


# 11..format(6)
a = "hello {}, I am {}".format("world","oxxo")
b = "hello {:10s}, I am {:10s}".format("world","oxxo")
c = "hello {:>10s}, I am {:>10s}".format("world","oxxo")
d = "hello {:-^10s}, I am {:+^10s}".format("world","oxxo")
e = "hello {:-^10.3s}, I am {:-^10s}".format("world","oxxo")
f = "hello {:-^10.3s}, I am {:^10.3f}".format("world",123.456789)
print(a)  # hello world, I am oxxo
print(b)  # hello world     , I am oxxo
print(c)  # hello      world, I am       oxxo
print(d)  # hello --world---, I am +++oxxo+++
print(e)  # hello ---wor----, I am ---oxxo---
print(f)  # hello ---wor----, I am  123.457


# 12.f-string(1)
# f{變數名稱或運算式}
a = "world"
b = "oxxo"
c = f"hello {a}, I am {b}"
print(c)   # hello world, I am oxxo


# 13.f-string(2)
a = "world"
b = "oxxo"
c = f"hello {a:<10s}, I am {b:>10s}"
d = f"hello {a:-<10s}, I am {b:+^10s}"
e = f"hello {a:-<10.3s}, I am {b:+^10.2s}"
f = f"hello {a.upper()}, I am {b.title()}"
print(c)   # hello world     , I am       oxxo
print(d)   # hello world-----, I am +++oxxo+++
print(e)   # hello wor-------, I am ++++ox++++
print(f)   # hello WORLD, I am Oxxo


# 14.f-string(3)
for i in range(1,101):
  print(f"{i:03d}",end=" , ")

'''
001 , 002 , 003 , 004 , 005 , 006 , 007 , 008 , 009 , 010 ,
011 , 012 , 013 , 014 , 015 , 016 , 017 , 018 , 019 , 020 ,
021 , 022 , 023 , 024 , 025 , 026 , 027 , 028 , 029 , 030 ,
031 , 032 , 033 , 034 , 035 , 036 , 037 , 038 , 039 , 040 ,
041 , 042 , 043 , 044 , 045 , 046 , 047 , 048 , 049 , 050 ,
051 , 052 , 053 , 054 , 055 , 056 , 057 , 058 , 059 , 060 ,
061 , 062 , 063 , 064 , 065 , 066 , 067 , 068 , 069 , 070 ,
071 , 072 , 073 , 074 , 075 , 076 , 077 , 078 , 079 , 080 ,
081 , 082 , 083 , 084 , 085 , 086 , 087 , 088 , 089 , 090 ,
091 , 092 , 093 , 094 , 095 , 096 , 097 , 098 , 099 , 100 ,
'''
