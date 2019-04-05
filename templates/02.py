class Person(object):


    def __init__(self,name):
        self.name=name


    def __str__(self):      #此条转义为anna，使他实例化，不写的话显示的是存放地址，与上必须空两行
        #return self.name                               #anna
        return '<{}:{}>'.format('Person',self.name)  #<Person:anna>
a = Person('anna')
print(a)