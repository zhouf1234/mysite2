from django.shortcuts import render,HttpResponse,redirect
#导入models这个模块，可使和models里的类关联
from . import models
from django.shortcuts import reverse

# Create your views here.

def users(request):
    #查询出所有的user,给他赋一个对象，一个对应一行数据,user_list是一个user对象列表，objects：目标
    #models.User.objects固定写法，关联的models的user类，即mysql的user这个表，以下操作都是针对models的class user类创建的mysql的表user
    user_list = models.User.objects.all()                     #全部
    user0 = models.User.objects.first()                         #第一个
    user1 = models.User.objects.filter(name='cici',age=18)    #筛选；多条件，单条件都可以的

    print(user_list)        #显示的是对象列表<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>]>
    print(user0)            #对象是User object (1)
    print(user1)            #对象<QuerySet [<User: User object (3)>]>
    print(user1[0].name)     #调取到user1的name,cici

    print(user_list[0].id)      #列表切片按下标0取到user表的id,name,age
    print(user_list[0].id,user_list[0].name,user_list[0].age)
    print('='*120)

    #filter处理后，即使传进去的是字典，调出来的返回的对象也是一个列表，也按列表的方法取其中的name或age
    arg_dict = {'name':'bobo','age':18}
    user2 = models.User.objects.filter(**arg_dict)  #把字典拆分成关键字参数传进去
    print(user2)                 #<QuerySet [<User: User object (2)>]>
    print(user2[0].name)        #bobo
    print('=' * 120)


    user3 = models.User.objects.get(id=3)#如果为id=4，mysql信息不存在，条件不满足，报错，少用，取一条
    print(user3.name)
    print('=' * 120)


    user4 = models.User.objects.filter(id=3)#如果为id=4，mysql信息不存在，显示没有此用户，多用，取多条
    if len(user4)>0:
        print(user4[0].name)
    else:
        print('没有此用户')
    print('=' * 120)


    user5 = models.User.objects.exclude(name='cici')  #排除,cici
    print(user5)                #<QuerySet [<User: User object (1)>, <User: User object (2)>]>
    print('=' * 120)

    #user12=models.Class0.objects.all().order_by('cname')  #按name排序升序
    #print(user12)

    #user9=models.Class0.objects.all().order_by('-first_day')  #降序排序,后加.reverse(）又会按升序
    #print(user9)

    #user7=models.Class0.objects.values_list('cname', 'first_day')  #列表对象全部元组显示方式
    #print(user7)

    #user8=models.Class0.objects.values('cname', 'first_day')    #列表中的字典对象
    #print(user8)

    #user10=models.Class0.objects.values('first_day').distinct() #达到first_day去重,只能单一去重
    #print(user10)

    #user11=models.Class0.objects.all().count()  #统计全部的有几条数据
    #print(user11)

    #user13=models.Class0.objects.exists()     #返回的是布尔值，表内有数据就True，没有数据就false
    #print(user13)

    #user14=models.Class0.objects.filter(id__gt=1)    #筛选id大于1的数据，这里面的_其实是两条_
    #print(user14)

    #user15=models.Class0.objects.filter(id__lt=5)   #筛选id小于5的数据
    #print(user15)

    #user16=models.Class0.objects.filter(id__in=[2, 5, 8])    #筛选id为2，5，8的cname数据，不存在则没有
    #print(user16)

    #user17=models.Class0.objects.filter(cname__contains='全栈') #关键字筛选：包含全栈的，区分英文大小写，如果要不区分，换icontains,加个i就行
    #print(user17)

    # user18=models.Class0.objects.filter(cname__icontains='...') #关键字筛选：换icontains,加个i就行,不区分大小写
    # print(user18)

    #user19=models.Class0.objects.filter(id__range=[2, 10])  #筛选id为2~10的所有cname
    #print(user19)

    #筛选年份为2018，月份为11的first_day的数据
    #user20=models.Class0.objects.filter(first_day__year=2018, first_day__month=11)
    #print(user20)

    #反向查询，一对一的表，通过表名反向找到student0的对象
    #us1=models.StudentDetall.objects.first().student0       # <Student0: anna>
    #us2=models.StudentDetall.objects.first().student0.sname  # 'anna'

    #跨表添加，查到class0的第一个对象，添加到teacher的tname为巴老师的cid里，也叫做变量传入，显示多一条数据
    #class_obj = models.Class0.objects.first()
    #us3=models.Teacher.objects.get(tname='巴老师').cid.add(class_obj)

    #全部添加，查到class0的所有对象，添加到teacher的tname为安老师的cid里
    #(*class_list)等同与for in遍历，把所有的cid都添加tname为安老师的cid里，显示增加了全部cid对象给安老师，多条
    #class_list = models.Class0.objects.all()
    #us4=models.Teacher.objects.get(tname='安老师').cid.add(*class_list)

    #追加，筛选到class0的id为2，10的对象，追加到tname为冯老师的cid里，显示多了两条数据teacher_id
    #add只能添加一个对象，加*强制分解才能传入，此次使用set强制追加这个方法
    #class_1 = models.Class0.objects.filter(id__in=[2, 10])
    #us5=models.Teacher.objects.get(tname='冯老师').cid.set(class_1)

    #清空，查到teacher的第一个id对象，在cid里清空其数据
    #us6=models.Teacher.objects.first().cid.clear()

    #清空，查到teacher的id=2的对象，在cid里清空其数据
    #us7=models.Teacher.objects.get(id=2).cid.clear()

    #指定删除一条，查到teacher的tname='巴老师'的对象，找到表里对应的tid，清除其cid为5的对象，少用
    #us8=models.Teacher.objects.get(tname='巴老师').cid.remove(5)

    #筛选所有带龙的学生表的班级对象，显示的是所有名字带龙的学生的班级信息
    #us9=models.Class0.objects.filter(students__sname__contains='龙')

    #返回的字典类型（班级，学生名都有）,显示{'cname': '全栈2班', 'students__sname': 'anna'}......
    #双下划线的方法
    #us10=models.Class0.objects.values('cname', 'students__sname')
    #us11=models.Class0.objects.all().values('cname', 'students__detall__email')结果同上

    #返回字典类型（班级，email）,通过班级表查到所有的email，[{'cname': '全栈2班', 'students__detall__email': '111@qq.com'}....
    #us11=models.Class0.objects.values('cname', 'students__detall__email')

    #创建记录，即增删改查的增
    #方法一：生成数据并提交数组，crete：生成
    #new_user = models.User.objects.create(name='dada',age=24)
    #方法二：创建了数据，还要加save向数据库提交数据
    #new_user2 = models.User(name='evev',age=33)         #执行一次增加一个。。。
    #new_user2.save()

    # 创建记录，即增删改查的删
    models.User.objects.filter(name='dada').delete()

    #创建记录，即增删改查的改
    #方法一：按name查到数据库，改的是age，先查再改
    #models.User.objects.filter(name='evev').update(age=44)
    #方法二：按name查到数据库，相同名字改掉第一个，save提交
    user6 = models.User.objects.filter(age=44).first()
    user6.name = 'feifei'
    user6.save()

    return render(request,'user_list.html',{'user_list':user_list})


#def classs(request):
    #class_list = models.Class2.objects.all()
    #print(class_list)
    #return render(request, 'class_list1.html', {'class_list': class_list})
#def students(request):
    #student_list = models.Student1.objects.all()
    #print(student_list)
    #return render(request, 'student_list1.html', {'student_list': student_list})

#orm方法sql数据库取到数据
def class_list(request):
    class_list = models.Class0.objects.all()
    return render(request, 'class_list.html', {'class_list': class_list})

#orm方法sql数据库删除班级
def delete_list(request):
    class_id = request.GET.get("class_id")
    models.Class0.objects.get(id=class_id).delete()
    return redirect(reverse("class_list"))

#orm方法sql数据库添加班级
def add_class(request):
    if request.method == 'POST':
        cname=request.POST.get('cname')
        first_day = request.POST.get('first_day')
        models.Class0.objects.create(cname=cname,first_day=first_day)
        return redirect(reverse("class_list"))
    return render(request,'add_list.html')

#orm方法sql数据库编辑班级,此处不用正则表达式的方法,edit_list的html已经因为下方的正则方法改过了
def edit_class1(request):
    #上传修改好的数据
    if request.method == 'POST':
        #上传数据
        id=request.POST.get('id')
        cname=request.POST.get('cname')
        first_day = request.POST.get('first_day')

        #更新数据库信息,get是一个一个更新，最后save（）提交，方法一：
        #class_obj=models.Class0.objects.get(id=id)
        #class_obj.cname=cname
        #class_obj.first_day=first_day
        #class_obj.save()

        # 更新数据库信息,一条更新，filter筛选，按id去查多条，update来改，方法二：
        models.Class0.objects.filter(id=id).update(cname=cname,first_day=first_day)
        #更新完信息后，跳转回主页面
        return redirect(reverse("class_list"))
    #取数据，此处的’class_id‘是后台的class_id=1/2/3。。。之意，主HTML设置了
    class_id = request.GET.get('class_id')
    #按id取一条数据，包括id，cname,first_day，取到的其实就是一个对象，在html里面不用使用for in遍历了
    class_obj=models.Class0.objects.get(id=class_id)
    #下方的{“class”}这个变量传进去edit_list.html里面，html里面的要用则value="{{class.id}}取id，不用遍历
    return render(request, 'edit_list.html',{"class":class_obj})

#修改班级信息
def edit_class(request,arg):
    if request.method == 'POST':
        id=request.POST.get('id')
        cname=request.POST.get('cname')
        first_day = request.POST.get('first_day')
        models.Class0.objects.filter(id=id).update(cname=cname, first_day=first_day)
        return redirect(reverse('class_list'))

    print("ok",arg)
    class_obj = models.Class0.objects.get(id=arg)
    return render(request, 'edit_list.html', {"class": class_obj})


#单表查询实例,因为在setting写了logger实例，可以查看到orm语句翻译后的sql语句ret下方
#SELECT `app01_class0`.`id`, `app01_class0`.`cname`, `app01_class0`.`first_day` FROM `app01_class0`  LIMIT 21; args=()
#models里写了def__str__实例化，所以此时的ret们显示的不会是query对象
def test(request):
    ret = models.Class0.objects.all()   #反馈的是queryset对象，一些对象组成的列表
    ret2 = models.Class0.objects.get(id=4)   #因为之前删除操作删过id=1，此次写存在的id
    print(ret)
    print('='*120)
    print(ret2)
    return HttpResponse('OK')

#学生表
def student_list(request):
    student_list=models.Student0.objects.all()
    #{'student_list':student_list},模板语言，可以在这个html里用student_list这个对象,是键值对
    #{'student_list':student_list},传进来的是student_list，既是上方的student_list=models.Student0.objects.all()的对象
    return render(request,'student_list.html',{'student_list':student_list})

#学生表删除
def delete_student(request,sid):
    #从数据库里面取id值为sid的学生对象,看路径的正则，显示在地址栏的sid，点到哪里就是哪一个的意思
    models.Student0.objects.get(id=sid).delete()
    return redirect(reverse('student_list'))

#添加学生表,第一种方法
def add_student(request):
    #上传进数据库
    if request.method == 'POST':
        sname = request.POST.get('sname')
        cid = request.POST.get('cid')

        #数据库的cid_id是class0.id对象,orm语句添加，之后跳转回主页面student_list，第一种方法
        #models.Student0.objects.create(sname=sname,cid_id=cid)

        #第二种orm语句，理解方便些，数据库的cid对象是级联了class0的id，所以class_obj语句
        class_obj = models.Class0.objects.get(id=cid)
        models.Student0.objects.create(sname=sname,cid=class_obj)

        return redirect(reverse('student_list'))
    #add_student表里下拉列表传进的是班级名，所以取的是Class0的对象
    class_list=models.Class0.objects.all()
    return render(request,'add_student.html',{'class_list':class_list})

#编辑学生表：第一种方法
#def edit_student(request,sid):
    # 填好的上传进数据库
    #if request.method == 'POST':
        #id = request.POST.get('id')
        #sname = request.POST.get('sname')
        #cid = request.POST.get('cid')
        #models.Student0.objects.filter(id=id).update(sname=sname,cid_id=cid)
        #return redirect(reverse('student_list'))

    #要知道现在编辑的是哪位学生,所以写了sid这个参数，跟删除学生表同理
    #取数据，要上传到edit的html的class_list，要获取的学生id：student_obj,
    #class_list = models.Class0.objects.all()
    #student_obj= models.Student0.objects.get(id=sid)
    #return render(request,'edit_student.html',{'class_list':class_list,'student':student_obj})

#编辑学生表：第二种方法
def edit_student(request,sid):
    student_obj= models.Student0.objects.get(id=sid)
    # 填好的上传进数据库
    if request.method == 'POST':
        sname = request.POST.get('sname')
        cid = request.POST.get('cid')
        #更新student_obj,然后save()提交；下面的cid是班级对象
        student_obj.sname=sname
        student_obj.cid_id=cid
        student_obj.save()
        return redirect(reverse('student_list'))

    #要知道现在编辑的是哪位学生,所以写了sid这个参数，跟删除学生表同理
    #取数据，要上传到edit的html的class_list，要获取的学生id：student_obj,
    class_list = models.Class0.objects.all()

    return render(request,'edit_student.html',{'class_list':class_list,'student':student_obj})


def teacher_list(request):
    teacher_list = models.Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teacher_list': teacher_list})

def add_teacher(request):
    if request.method == 'POST':
        tname = request.POST.get('tname')
        class_ids = request.POST.getlist('cid')

        teacher_obj=models.Teacher.objects.create(tname=tname)
        teacher_obj.cid.add(*class_ids)
        return redirect(reverse('teacher_list'))
    class_list=models.Class0.objects.all()
    return render(request,'add_teacher.html',{'class_list':class_list})


def delete_teacher(request,tid):
    models.Teacher.objects.get(id=tid).delete()
    return redirect(reverse('teacher_list'))

def edit_teacher(request,tid):
    teacher_obj = models.Teacher.objects.get(id=tid)
    if request.method == 'POST':
        tname = request.POST.get('tname')
        class_ids = request.POST.getlist('cid')

        teacher_obj.tname=tname
        teacher_obj.cid.set(class_ids)
        teacher_obj.save()
        return redirect(reverse('teacher_list'))

    class_list=models.Class0.objects.all()
    return render(request, 'edit_teacher.html', {'class_list': class_list,'teacher':teacher_obj})