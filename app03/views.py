from django.shortcuts import render
from django import forms
from django.forms import fields
from django.forms import widgets
# Create your views here.
class TestForm(forms.Form):
    user = fields.CharField(
        required=True,#是否必填
        max_length=12,#最大长度
        min_length=3,#最小长度
        error_messages={},#错误提示,
        # widget = widgets.Textarea(),#定制生成的HTML插件 功能很强大
        # widget2 = widgets.Select(),#定制生成的HTML插件 功能很强大
    )
    age = fields.IntegerField()
    email = fields.EmailField()
def test(request):
    obj = TestForm()
    return render(request,'test.html',locals())