from django.db import models

# Create your models here.
#class user:创建的表的名字，等同于数据库里的create_table user,新建了一个表
class User(models.Model):
    #int auto_increment,primary_key
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)              #varchar(32)，不写null=True即默认不能为空
    age = models.IntegerField()                         #int数据类型
    class Meta:
        db_table = "User"                              #此条class类函数语句意思为建立的表格改名为User

class Book(models.Model):                             #book:原始表名
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64,null=True)    #varchar(64),写了null=True即是可以设置为空，不写字
    #price =models.IntegerField(null=True)               #设置sql数据库的price一栏可以为空，自行输入
    price = models.IntegerField(default=29)             #设置sql数据库的price一栏定值为29
    class Meta:
        db_table = "Book"

#创建mysql班级表
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=64,null=True)
    class Meta:
        db_table = "Class"

#创建mysql学生表
class Student2(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32,null=True)
    cid = models.IntegerField(null=True)
    #cid = models.ForeignKey(Student,on_delete=None)#和上方class的id做联查的一个语句,此处无效了解，按最下学生表的按原始表名关联键
    class Meta:
        db_table = "Student"


class Class2(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32,null=True)
    class Meta:
        db_table = "Class2"

class Student1(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32,null=True)
    cid = models.IntegerField(null=True)
    class Meta:
        db_table = "Student2"

class Class0(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32)
    first_day = models.DateField()               #显示的是日期，英文显示的

    #此处使实例化< QuerySet[ < Class0: 全栈2班 | 2018 - 11 - 06 >, < Class0: 全栈四班 | 2018 - 11 - 03 >,。。。
    #改掉了format（self.first_day）就没有日期了，见01.py文件例
    def __str__(self):
        return self.cname

class Student0(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32)
    #此处cid对应的是class0对象，student0对象；cid取到班级对象，然后可以通过student.cid.cname去操作
    #student.cid_id就是class0.id对象;related_name='students'取别名，不影响引用的，用于反向查找，一找多
    cid = models.ForeignKey(to="Class0",to_field="id",on_delete=models.CASCADE,related_name='students')
    #unique=True使数据关系只能一对一，即一个学生的信息只能对应一个学生,不可重复
    #detall = models.ForeignKey(to="StudentDetall",on_delete=models.CASCADE,unique=True)

    #null=True：允许它可以空值，不然manage.py的输入框makemigrations会提示
    detall = models.OneToOneField(to="StudentDetall",on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.sname

class StudentDetall(models.Model):
    height = models.PositiveSmallIntegerField()   #不直接用IntegerField，是因为int包含了负数的
    email = models.EmailField()
    memo = models.CharField(max_length=128,null=True)

#第一种方法，第三张表TeacherToClass来关联老师表和班级表，建立了两张表,此次都未执行
#不能使用django ORM的多对多操作语法
#class Teacher(models.Model):
    #tname = models.CharField(max_length=32)

#class TeacherToClass(models.Model):
    #tid和cid都通过外键关联，做级联操作，id不写，让他自动生成，上方的class studentdetall也没写
    #tid = models.ForeignKey(to='Teacher',on_delete=models.CASCADE)
    #cid = models.ForeignKey(to='Class0',on_delete=models.CASCADE)
    #class Meta:
        #unique_together = ('tid','cid')   #unique:唯一性，使tid，cid只能输入一次，不可重复

#第二种方法,写一个class teacher，执行后diango ORM帮我们自动生成一个teacher_id的表，也是相当于有两个表
#自动生成的类teacher_id，没有类和他对应，即：不能通过ORM的class类单独操作这个表
class Teacher(models.Model):
    tname =models.CharField(max_length=32)
    cid = models.ManyToManyField('Class0',null=False)

#第三种方法：前两种方法的折中，同第一种方法差不多的，也是自己建立了两张表，尽量多用第二种方法
#和第一种的一样，很多django语言无法使用
#class Teacher(models.Model):
    #tname =models.CharField(max_length=32)
    #through属性表示要和这张表做关联，也可以写to属性
    #如果写这个属性through_field=('tid','cid')，即是关联TeacherToClass表的字段，也少用
    #cid = models.ManyToManyField(through='TeacherToClass',through_field=('tid','cid'))