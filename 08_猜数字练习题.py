

num = 10
if int(input("请输入第一次猜想的数字：")) == num:
    print("啥阴间，第一次就蒙对了？？")
elif int (input("不对，再猜一次：")) == num:
    print("第二次猜到了，有点意思...")
elif int (input("不对，再猜最后一次：")) == num:
    print("第三次猜到了，差点你就输了..")
else:
    print("垃圾，you should gonna die,bro.")
