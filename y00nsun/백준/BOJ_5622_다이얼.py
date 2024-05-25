# BOJ
# 5622: 다이얼

w = input()

result = []
for s in w:
    if s == " ":
        result.append(1)
    elif s in ["A", "B", "C"]:
        result.append(2)
    elif s in ["D", "E", "F"]:
        result.append(3)
    elif s in ["G", "H", "I"]:
        result.append(4)
    elif s in ["J", "K", "L"]:
        result.append(5)
    elif s in ["M", "N", "O"]:
        result.append(6)
    elif s in ["P", "Q", "R", "S"]:
        result.append(7)
    elif s in ["T", "U", "V"]:
        result.append(8)
    elif s in ["W", "X", "Y", "Z"]:
        result.append(9)
    else:
        result.append(0)

sum = 0
for i in result:
    if int(i) == 0:
        sum += 11
    sum += int(i) + 1
print(sum)