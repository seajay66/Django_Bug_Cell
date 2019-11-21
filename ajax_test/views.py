from django.shortcuts import render,HttpResponse
import json,time,os
import uuid
# Create your views here.
def ajax_test1(request):
    return render(request,'ajax_test1.html')


def ajax_test2(request):
    time.sleep(1)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    # print(request.body)
    ret = {'status':True,'message':'要成功'}
    return HttpResponse(json.dumps(ret))

def upload_ajax(request):
    return render(request, 'upload1.html')

def upload_scan(request):
    return render(request,'upload_scan.html')

def upload_img(request):
    nid = str(uuid.uuid4())
    ret = {'status':True,'data':None,'message':None}
    # 接受文件并写到本地
    obj = request.FILES.get('k3')
    file_path = os.path.join('static',nid+obj.name)
    f = open(file_path,'wb')
    for line in obj.chunks():
        f.write(line)
    f.close()
    ret['data']= file_path
    return HttpResponse(json.dumps(ret))

def jsonp(request):
    return render(request,'jsonp.html')

def ajax3(request):
    return HttpResponse('本服务器发送的请求')