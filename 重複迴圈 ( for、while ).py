# 1.for 迴圈(1)
# for 迴圈內容執行的程式區塊，採用縮排的方式。
for i in "abc":
    print(i)    # a  b  c ( 字串 )

for i in ["a","b","c"]:
    print(i)    # a  b  c ( 串列 )

for i in {"a","b","c"}:
    print(i)    # c  b  a ( 集合 )

for i in {"a":1,"b":2,"c":3}:
    print(i)    # a  b  c ( 字典 )


# 2.for 迴圈(2)
for a in ["x","y","z"]:
    for b in [1,2,3]:
        print(b)
    print(a)

# 1 2 3 x 1 2 3 y 1 2 3 z


# 3.for 迴圈(3)
for a in ["x","y","z"]:
    for b in [1,2,3]:
        print(f"{a}{b}")

# x1 x2 x3 y1 y2 y3 z1 z2 z3


# 4.while 迴圈
# while 迴圈內容執行的程式區塊，採用縮排的方式 。
a = 1
while a <= 5:
    print(a)
    a += 1

# 1 2 3 4 5


# 5.break 和 continue(1)
for a in ["x","y","z"]:
    for b in [1,2,3]:
        if(b == 2):
            break
        print(f"{a}{b}")
print("ok")

# x1 y1 z1 ok


# 6.break 和 continue(2)
for a in ["x","y","z"]:
    for b in [1,2,3]:
        if(b == 2):
            continue
        print(f"{a}{b}")
print("ok")

# x1 x3 y1 y3 z1 z3 ok
