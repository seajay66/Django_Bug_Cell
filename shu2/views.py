from django.shortcuts import render,HttpResponse,redirect
from shu2 import models

#用下面语句 进行验证用户提供的信息
from django import forms
from django.forms import fields

class F1Form(forms.Form):
    # 对应前端的input的name属性 所以下面的u p a e 都不用写了
    #下面的error_messages 为自定义错误提示：
    user = fields.CharField(
        max_length=18,
        min_length=6,
        required=True,
        error_messages={
            'required':'用户名不能为空啊',
            'max_length':'太长了',
            'min_length':'太短了',
        }
    )
    #注意 格式错误的  都为invalid错误提示：
    pwd = fields.CharField(min_length=32)
    age = fields.IntegerField(
        required=True,
        error_messages={
            'required':'年龄不能为空',
            'invalid':'格式错误，请重新输入',
        }
    )
    email = fields.EmailField(required=True)



# Create your views here.
def f1(request):
    if request.method == 'GET':
        obj = F1Form() #如果前后端 容易出错 前端页面的name属性在后端命名出错，则无法验证用户输入的正确与否。所以要用到Form组件的生成代码功能！
        # 将obj一个实例化的对象传入HTML前端 -->
        #这样还有一个优势好处是，提交后的数据，还在输入框内显示着；
        return render(request,'f1.html',{'obj':obj})
    else:
        # u = request.POST.get("user") # 不能为空 长度6-18
        # p = request.POST.get("pwd") # 不能为空，长度32
        # e = request.POST.get("email")# 必须为邮箱格式
        # a = request.POST.get("age") #不能为空 必须为数字
        # # 1、检查是否为空
        # # 2、检查格式是否正确
        # print(u,p,e,a)
        # #创建一个类；类中创建字段，字段中包含正则表达式。
        obj = F1Form(request.POST) #django自动根据name属性进行与类中规则进行比对
        if obj.is_valid(): #产生的结果就是 是否验证成功
            print(obj.cleaned_data) # 已经验证成功的数据 用户提交的数据；
            print("验证成功")
            return redirect('http://www.baidu.com')
        else:
            print(obj.errors)
            print("验证失败")
        return render(request,"f1.html",{'obj':obj})

def users(request):
    user_list = models.UserInfo.objects.all()
    return render(request,'uers.html',locals())


from shu2.forms import UserForm
def add_user(request):
    if request.method =="GET":
        obj = UserForm()
        return render(request,'add_user.html',{'obj':obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            # 注意 下面这行 为快捷将用户输入的数据存入数据库的方法  **obj
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/users/')
        else:
            return render(request, 'add_user.html', {'obj': obj})
def edit_user(request,nid):
    if request.method == 'GET':
        # nid = request.GET.get('nid')
        data = models.UserInfo.objects.filter(id=nid).first()
        obj = UserForm({'username':data.username,'email':data.email})
        return render(request,'edit_user.html',{'obj':obj,'nid':nid})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/users/')
        else:
            return render(request, 'edit_user.html', {'obj': obj, 'nid': nid})