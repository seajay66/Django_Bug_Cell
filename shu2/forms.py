from django import forms as dforms
from django.forms import fields
class UserForm(dforms.Form):
    username = fields.CharField(min_length=5)
    email = fields.EmailField()