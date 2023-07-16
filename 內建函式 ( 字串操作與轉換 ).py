# 1.str(x)
# 將參數 x 轉換成文字型別，不論是數字、串列、tuple、布林，都會變成純文字。
a = str(123)
b = str([1,2,3])
c = str(True)
d = str(False)
print(a)     # 123
print(b)     # [1,2,3]
print(b[0])  # [ ( 因為是純文字，第一個字母就是 [ )
print(c)     # True
print(d)     # False
print(c+d)   # TrueFalse ( 因為是純文字，變成字串的相加 )


# 2.ascii(x)
# 將參數 x 轉換成 ASCII 碼。
a = ascii("你好")
print(a)    # '\u4f60\u597d'


# 3.bin(x)
# 將參數 x 的數字，轉換成二進位的字串。
a = bin(1234)
print(a)    # 0b10011010010


# 4.oct(x)
# 將參數 x 的數字，轉換成八進位的字串。
a = oct(1234)
print(a)    # 0o2322


# 5.hex(x)
# 將參數 x 的數字，轉換成十六進位的字串。
a = hex(1234)
print(a)    # 0x4d2


# 6.chr(x)
# 將參數 x 轉換為所代表的 Unicode 字元。
a = chr(101)
b = chr(202)
c = chr(9999)
print(a)    # e
print(b)    # Ê
print(c)    # ✏


# 7.ord(x)
# 將參數 x 所代表的 Unicode 字元，轉換為對應編碼數字。
a = ord("e")
b = ord("Ê")
c = ord("✏")
print(a)    # 101
print(b)    # 202
print(c)    # 9999
