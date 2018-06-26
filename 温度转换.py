a = input()
if a[0] in ["f","F"]:
    # 把字符串的前面所有字符（除去最后一个）变成整数或者浮点数
    C = (eval(a[1:]) - 32)/1.8
    # 保存为两位小数输出,format=格式
    print("C{:.2f}".format(C))
elif a[0] in ["C","c"]:
    F = eval(a[1:])*1.8+32
    print("F{:.2f}".format(F))
else:
    print("type error")

