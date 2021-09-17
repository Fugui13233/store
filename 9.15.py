# 任务一：
# #1、实现输入10个数字，并打印10个数的求和结果
# a=int(input("请输入你的第一个数："))
# b=int(input("请输入你的第二个数："))
# c=int(input("请输入你的第三个数："))
# d=int(input("请输入你的第四个数："))
# e=int(input("请输入你的第五个数："))
# f=int(input("请输入你的第六个数："))
# g=int(input("请输入你的第七个数："))
# h=int(input("请输入你的第八个数："))
# i=int(input("请输入你的第九个数："))
# j=int(input("请输入你的第十个数："))
# num=a+b+c+d+e+f+g+h+i+j
# print("总和为：%s"%num)


# 2、从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# a=int(input("请输入你的第一个数："))
# b=int(input("请输入你的第二个数："))
# c=int(input("请输入你的第三个数："))
# d=int(input("请输入你的第四个数："))
# e=int(input("请输入你的第五个数："))
# f=int(input("请输入你的第六个数："))
# g=int(input("请输入你的第七个数："))
# h=int(input("请输入你的第八个数："))
# i=int(input("请输入你的第九个数："))
# j=int(input("请输入你的第十个数："))
# max=max([a,b,c,d,e,f,g,h,i,j])
# sum=a+b+c+d+e+f+g+h+i+j
# average=(a+b+c+d+e+f+g+h+i+j)/10
# print("最大数为：%s"%max)
# print("10个数的和为：%s"%sum)
# print("平均数为：%s"%average)

# 3、使用random模块，如何产生 50~150之间的数？
# import random
# ran=random.randint(50,150)
# print("随机数为：%s"%ran)

# 4、从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a=int(input("请输入边长："))
# b=int(input("请输入边长："))
# c=int(input("请输入边长："))
# if a < b+c and b < a+c and c < a+b:
#     print("能形成三角形！")
#     if a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
#         print("能形成直角三角形")
#     elif a == b or b == c or a == c:
#         if a == b == c:
#             print("等边三角形！")
#         else:
#             print("能组成等腰三角形")
#     else:
#         print("能组成普通三角形！")
# else:
#     print("不能形成三角形!")


# 5、有以下两个数，使用+，-号实现两个数的调换。
# A=56
# B=78
# 实现效果：
# A=78
# B=56
# a=input("请输入+或者-:")
# while a=="+" or a=="-":
#     if a=="+":
#         print("A=78")
#         break
#     elif a=="-":
#         print("B=56")
#         break
#     else:
#         break
# else:
#     print("输入+或者-！")


# 6、实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# count=0
# a="root"
# b="admin"
# while count<3:
#     count += 1
#     c=str(input("请输入用户名："))
#     d=str(input("请输入密码："))
#     if a==c and b==d:
#         print("登录成功！")
#         break
#     else:
#         print("请重新输入！")
# else:
#     print("机会已用尽！")



# 7、编程实现下列图形的打印
#     *
#    ***
#   *****
# i = 0
# while i < 9:
#     if i < 5:
#         j = 0
#         while j < 4 - i:
#             print(" ", end="")
#             j += 1
#         j = 0
#         while j < i + 1:
#             print("*", end=" ")
#             j += 1
#     print()
#     i += 1

# 8、使用while循环实现99乘法表的打印。
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={j*i}",end="\t")
#         j+=1
#     print()
#     i+=1

# 9、编程实现99乘法表的倒叙打印
# for i in range(1,10):
#    for j in range(i,10):
#        print("%d*%d=%2d" % (i,j,i*j),end=" ")
#    print("")



# # 10、一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# day=1
# a=3
# b=2
# sum=0
# while sum+a<20:
#     sum=sum+a-b
#     day+=1
# print("在第%s天的时候能出来!"%day)







# 11、继续完成上午的猜数字游戏的需求功能。
# 1.添加计数打印功能
# 2.添加次数金币功能和锁定系统功能。
# import random
# play=input("准备好了吗？")
# random_num=random.randint(1,10)
# money=1000
# while play=="1":
#        print("游戏开始!")
#        money1 = int(input("请输入充值金额："))
#        money = money + money1 * 1.2
#        count=0
#        while count < 5:
#               count += 1
#               num=int(input("请输入你猜的数："))
#               if money>0:
#                      if num>random_num:
#                             print("你猜的有点大啊")
#                             print("还剩%s次机会"%(5-count))
#                             money=money-500
#                             print("余额为 ：%s" % money)
#                      elif num<random_num:
#                             print("猜小了猜小了")
#                             print("还剩%s次机会" %(5- count))
#                             money=money-500
#                             print("余额为 ：%s" % money)
#                      else :
#                             print("如果你没猜错的情况下，你一定是猜对了！")
#                             print("你一共用了%s次机会"%count)
#                             print("随机数字是%s"%num)
#                             money=money+2000
#                             print("余额为 ：%s"%money)
#                             break
#               else:
#                      print("余额不足！")
#                      break
#        break
# else:
#        print("游戏结束！")





# 12、用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）2432902008176640000
# product=1
# for i in range(1,21):
#     product=i*product
# print(product)
