from django.shortcuts import render,HttpResponse

# Create your views here.
def ajax_test1(request):
    return render(request,'ajax_test1.html')


def ajax_test2(request):
    print(request.GET)
    print(request.POST)
    print(request.body)
    return HttpResponse("...")