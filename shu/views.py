from django.shortcuts import render,redirect,HttpResponse
from shu.models import Industry, Cellphone
import time
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from shu.pager import Pagination
# Create your views here.
def cellphone(request):
    # models.Cellphone.objects.create(xinghao="小米8",pingmudaxiao=5,m_id=1)
    # models.Cellphone.objects.create(xinghao="小米9",pingmudaxiao=6,m_id=1)
    # models.Cellphone.objects.create(xinghao="小米10",pingmudaxiao=7,m_id=1)
    # models.Cellphone.objects.create(xinghao="苹果8",pingmudaxiao=6,m_id=2)
    # models.Cellphone.objects.create(xinghao="苹果8",pingmudaxiao=7,m_id=2)
    # models.Cellphone.objects.create(xinghao="魅族8",pingmudaxiao=10,m_id=3)
    cell_list = Cellphone.objects.all()
    return render(request,"cell.html",locals())
def add(request):
    if request.method == "GET":
        obj = Industry.objects.all()
        return render(request,"add_cell.html",locals())
    elif request.method == "POST":
        name = request.POST.get("new_cell_name")
        pingmudaxiao = request.POST.get("new_cell_screensizi")
        ceo1 = request.POST.get("new_CEO")
        print("拿到的ceo1是：",ceo1)
        new_id = Industry.objects.filter(CEO=ceo1).first().id
        # new_id = Industry.objects.filter(CEO=ceo).first().id # 报错说，无id属性
        #经查 上述问题的原因竟然是因为：HTML中option属性不能用value 应该用name传到后台来才行
        #但还是无法理解为何传回来的 也是字符串属性打印输出也没问题就是传参出错。。。
        Cellphone.objects.create(xinghao=name,pingmudaxiao=pingmudaxiao, m_id=new_id)
        return redirect("/cellphone")
def delete_ce(request):
    nid = request.GET.get("nid")
    Cellphone.objects.filter(id=nid).delete()
    return redirect("/cellphone")
def edit(request):
    if request.method == "GET":
        nid = request.GET.get("nid")
        edit_item = Cellphone.objects.filter(id=nid).first()
        industry_obj = Industry.objects.all()
        return render(request,"edit.html",locals())
    elif request.method == "POST":
        nid = request.GET.get("nid")
        edit_item = Cellphone.objects.filter(id=nid).first()
        industry_obj = Industry.objects.all()
        xh = request.POST.get("xinghao")
        pmdx = request.POST.get("pingmudaxiao")
        xuanze = request.POST.get("xuanze")

        #new_id = Industry.objects.filter(CEO=ceo1).first().id
        print(xuanze)
        new_id = Industry.objects.filter(CEO=xuanze).first().id
        print(nid,xh,pmdx)
        Cellphone.objects.filter(id=nid).update(xinghao=xh,pingmudaxiao=pmdx,m_id=new_id)
        return redirect("/cellphone")
def ajax1(request):
    return render(request,"ajax1.html")
def ajax2(request):
    user = request.GET.get("username")
    pwd = request.GET.get("password")
    time.sleep(2)
    c = int(user)+int(pwd)
    return HttpResponse(c)
USER_LIST = []
for i in range(1,999):
    temp = {
        "name":"root" + str(i),
        "age":i
    }
    USER_LIST.append(temp)
def index(request):
    # 这是简单的自己手写一个功能简单的分页工具
    try:
        current_page = request.GET.get('p')
        current_page = int(current_page)
    except Exception as e:
        current_page = 1
    # 每页显示10条数据
    par_page_count = 10
    # p = 1
    # 0,10   0-9
    # p = 2
    # 10,20 10-19
    start = (current_page-1)*10
    end = current_page*par_page_count
    data = USER_LIST[start:end]
    if current_page <=1:
        prev_page = 1
    else:
        prev_page = current_page - 1
    next_page = current_page + 1
    # return render(request,'index.html',{'user_list':data,'prev_page':prev_page,'next_page':next_page)
    # return HttpResponse('ok')
    return render(request,'index.html',{'user_list':data,'prev_page':prev_page,'next_page':next_page})
# 自己创建一个类 继承Paginator,来实现上一页下一页中间的页面的效果；
# 这样以后可以直接用自己写的这个继承django提供的这个即可。
class CustomPaginitor(Paginator):
    def __init__(self,current_page,per_page_number,*args,**kwargs):
        # 代指当前页
        self.current_page = int(current_page)
        # 代指最多显示页码的数量
        self.per_page_number = int(per_page_number)
        super(CustomPaginitor, self).__init__(*args,**kwargs)
    def pager_num_range(self):
        # 总页数 self.per_pager_num
        if self.num_pages < self.per_page_number:
            return range(1,self.num_pages+1)
        # 总页数特别多的时候
        part = int(self.per_page_number/2)
        if int(self.current_page) <= part:
            return range(1,self.per_page_number+1)
        if self.current_page+part >self.num_pages:
            return range(self.num_pages-self.per_page_number,self.num_pages+1)
        return range(int(self.current_page)-part,int(self.current_page)+part+1)
        # return range(1,12)

def index1(request):
    #这是利用django的内置分页工具
    #共计Paginator对象和Page两个对象。
    #为了页面简单，适合分出去一个include小页面。这样其它地方需要用分页，直接导入即可。这样代码少一些，可移植性强。
    # 已经引入了django自带分页的类 所以要先创建一个 对象
    # 拿到了所有数据  -->  得出共有多少条数据
    # 每页10条的话 总共有多少页 也就能够计算出来
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象（是否具有下一页；是否有上一页；）
    current_page = request.GET.get('p')
    # Paginator对象
    paginator = CustomPaginitor(current_page,11,USER_LIST,10)
    try:
        # Page对象
        posts = paginator.page(current_page)
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表，已经切片好的数据
        # number                当前页
        # paginator             paginator对象
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,"index1.html",{'posts':posts})
def index2(request):
    current_page = request.GET.get("p")
    page_obj = Pagination(999,current_page)
    data_list = USER_LIST[page_obj.start():page_obj.end()]
    return render(request,"index2.html",{'data_list':data_list,'page_obj':page_obj})