from threading import Thread
import time
tart=0
class eag_tart(Thread):
    cook=""
    count=0
    def run(self)->None:
        global tart
        while True:
            if tart>=500:
                time.sleep(3)
            else:
                tart=tart+1
                self.count=self.count+1
                print(self.cook,"造了",self.count,"个蛋挞！篮子里有",tart,"个蛋挞")

class tartl(Thread):
    consumers=""
    money=3000
    count=0
    def run(self) ->None:
        global tart
        while True:
            if tart<1:
                time.sleep(3)
            elif tart>0 and self.money>=0:
                tart=tart-1
                self.money=self.money-2
                self.count=self.count+1
                print(self.consumers,"抢了",self.count,"个蛋挞!")
            elif self.money<0:
                print("余额不足")
                break

a1=tartl()
a2=tartl()
a3=tartl()
a4=tartl()
a5=tartl()
a6=tartl()
a7=eag_tart()
a8=eag_tart()
a9=eag_tart()
a1.consumers="韩"
a2.consumers="赵"
a3.consumers="魏"
a4.consumers="楚"
a5.consumers="燕"
a6.consumers="齐"
a7.cook="魏"
a8.cook="蜀"
a9.cook="吴"
a1.start()
a2.start()
a3.start()
a4.start()
a5.start()
a6.start()
a7.start()
a8.start()
a9.start()





