from django.shortcuts import render,redirect
from shu.models import Industry, Cellphone
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
