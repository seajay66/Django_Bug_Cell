from django.shortcuts import render,HttpResponse

# Create your views here.
# 简单的文件上传
def upload(request):
    if request.method == "GET":
        return render(request,'upload.html')
    else:
        print(request.POST)
        print(request.FILES)
        user = request.POST.get("user")
        img = request.FILES.get('img')
        print(img.name,img.size)
        print(user)
        if img.size < 6000:
            f = open(img.name,'wb')
            for line in img.chunks():
                f.write(line)
            f.close()
        else:
            print('您上传的文件过大，请重新上传')
        return HttpResponse('ok')