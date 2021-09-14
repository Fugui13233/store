# 猜随机数
import random
play=input("准备好了吗？")
random_num=random.randint(1,10)
money=1000
while play=="1":
       print("游戏开始!")
       money1 = int(input("请输入充值金额："))
       money = money + money1 * 1.2
       count=0
       while count < 5:
              count += 1
              num=int(input("请输入你猜的数："))
              if money>0:
                     if num>random_num:
                            print("你猜的有点大啊")
                            money=money-500
                     elif num<random_num:
                            print("猜小了猜小了")
                            money=money-500
                     else :
                            print("如果你没猜错的情况下，你一定是猜对了！")
                            print("随机数字是%s"%num)
                            money=money+2000
                            print("余额为 ：%s"%money)
                            break
              else:
                     print("余额不足！")
                     break
       break
else:
       print("游戏结束！")





