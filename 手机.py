'''
    老手机：
        打电话：手机号，彩铃
    新手机：
        打电话：手机号，彩铃，归属地，大头贴，录音
'''
import time
# class OldPhone:
#     phoneNumber = ""
#     voice = ""
#
#     def call(self,number):
#         print(self.phoneNumber,"正在打电话，打给：",number,"正在响铃：",self.voice)
#         for i  in range(8):
#             print(".",end="")
#             time.sleep(1)
#         print("对方已接通！！")
#
# class NewPhone(OldPhone):
#     # 归属地，大头贴，录音
#     address = ""
#     picture = ""
#     mic = False
#
#     def call(self,number):
#         # 2个属性由老手机代码显示
#         super().call(number)
#
#         # 3个新属性由新手机自己显示
#         self.mic = True
#         print("本机归属地：",self.address,"，对方大头贴为：",self.picture,",已经开启了录音功能！")
#         for i in range(8):
#             print(".",end="")
#             time.sleep(1)
#         print("本次通话完成[5:36]！")


# phone = NewPhone()
# phone.phoneNumber = "13552648187"
# phone.voice = "江南style"
# phone.picture = "野猪佩奇"
# phone.address = "北京移动"
#
# phone.call("13379854676")


#
# 按要求定义类
# 考查知识点：super关键字的使用和继承中方法的调用
# 要求：
# 1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
# 2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
# 3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
# 4、使用新手机对象调用手机介绍的方法；
# 5、使用新手机对象调用打电话的方法；
class oderP:
    __brand = ""
    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand

    def call(self, number):
        print("正在打给：",number)
        for i in range(8):
            print(".",end="")
            time.sleep(1)
        print("对方已接通！！")
        print("品牌为",self.__brand,"的手机真好用")

class newP(oderP):
    def call(self,number):
        super().call(number)


i=newP()
i.setBrand="小米"
i.call("13872031732")


# 题目一：
# 考查知识点：继承的传递性
# 按要求定义类
# 要求：
# 1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
# 2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
# 3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
# 4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
# 5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；

# class cook:
#     __name=""
#     __age=""
#     def setName(self,name):
#         self.__name=name
#     def getName(self):
#         return self.__name
#     def setAge(self,age):
#         self.__age=age
#     def getAge(self):
#         return self.__age
#     def stir_fry(self):
#         print("我是一名厨师，叫",self.__name,"年龄是",self.__age,"我正在炒菜")
# class cooks(cook):
#     def stir_fry(self):
#         super().stir_fry()
# class cookses(cooks):
#     def steamed_rice():
#
#         print("我是一名厨师，叫",self.__name,"年龄是",self.__age,"我正在蒸饭")
#
# b=cooks()
# b.setName("李刚")
# b.setAge(45)
# b.stir_fry()
#
# d=cookses()
# d.steamed_rice()





#
# 请编程
# i.人：年龄，性别，姓名。
# ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
# iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
#
class people:
    age=""
    sex=""
    name=""
class type_of_work(people):
    def type_work(self):
        print("一个叫",self.name,"性别为",self.sex,"性,年龄为",self.age,"岁的工人在干活")
class student(people):
    student_id=None
    def doing(self,study,song):
        print("一个叫",self.name,"性别为",self.sex,"性,年龄为",self.age,"岁,学号为",self.student_id,"的学生在",study,song)

a=type_of_work()
a.name="李刚"
a.sex="男"
a.age=81
a.type_work()

c=student()
c.name="小明"
c.sex="男"
c.age=19
c.student_id="1655646"
c.doing("学习","唱歌")
