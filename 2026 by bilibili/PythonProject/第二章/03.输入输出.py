#input(..) 所有键盘录入的数据格式都是string
# name = input("请输入您的姓名：")
# age = input("请输入您的年龄：")
#
# print(f"姓名：{name} ，年龄：{age}")

#案例：ATM取款
# 1.输入密码
password = input("请输入您的银行卡密码：")
if password == "123456":
    amount = 10000
    print(f"当前银行卡余额：{amount}")
    #2.输入取款金额
    num1 = input("请输入您的取款金额：")
    #3.计算剩余金额
    num2 = float(amount) - float(num1)
    print(f"当前银行卡余额：{num2}")
else:
    print("密码错误")