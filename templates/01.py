class Car(object):

    def __init__(self,name,speed,color):
        self.name = name
        self.speed = speed
        self.color = color

    def special(self):
        return "这辆车车名是{},车速是{},颜色是{}".format(self.name,self.speed,self.color)

a = Car("劳斯莱斯","200码","红色")
b = Car("奔驰","220码","白色")

print(b.special())