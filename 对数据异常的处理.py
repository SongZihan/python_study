guest_01 = input("请输入第一个数字：")
error_number = ("您所输入的不是数字")
try:
    guest_01 = int(guest_01)
except ValueError:
    print(error_number)
else:
    guest_02 = input("请输入第二个数字：")
    try:
        guest_02 = int(guest_02)
    except ValueError:
        print(error_number)
    else:
        guest_03 = guest_01 + guest_02
        print("他们的和是{:}".format(guest_03))


