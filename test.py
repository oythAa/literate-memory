while True:
    num = input("请输入一个三位自然数：")
    # 判断是否全是数字，并且长度为3
    if num.isdigit() and len(num) == 3:
        n = int(num)
        break
    print("输入不合法！必须是3位自然数，请重新输入\n")

hundred = n // 100        # 百位
ten = n // 10 % 10        # 十位
unit = n % 10             # 个位

print(f"百位：{hundred}")
print(f"十位：{ten}")
print(f"个位：{unit}")