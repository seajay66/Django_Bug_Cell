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
        obj = Industry.objects.all()
        name = request.POST.get("new_cell_name")
        pingmudaxiao = request.POST.get("new_cell_screensizi")
        ceo111 = request.POST.get("new_CEO")
        niddd=request.POST.get("name")
        print("检测",ceo111,type(ceo111))
        eee = "雷军"
        print(type(eee))
        new_id = Industry.objects.filter(CEO=eee).first().id
        print(new_id)
        ceo=ceo111
        # new_id = Industry.objects.filter(CEO=ceo).first().id # 报错说，无id属性
        new_id_2 = Industry.objects.filter()

        # print(new_id,type(new_id))
        # print(new_id_2,type(new_id_2))
        # print(new_id_2,type(new_id))


        Cellphone.objects.create(xinghao=name,pingmudaxiao=pingmudaxiao, m_id=new_id)
        return redirect("/cellphone")
def delete_ce(request):
    nid = request.GET.get("nid")
    Cellphone.objects.filter(id=nid).delete()
    return redirect("/cellphone")