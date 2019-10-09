from django.db import models

# Create your models here.
class Cellphone(models.Model):
    xinghao = models.CharField(max_length=32)
    pingmudaxiao = models.IntegerField()
    m = models.ForeignKey("Industry", on_delete=False)

class Industry(models.Model):
    name = models.CharField(max_length=32)
    CEO = models.CharField(max_length=32)
    t = models.ManyToManyField("Gongyingshang")

class Gongyingshang(models.Model):
    title = models.CharField(max_length=32)
    provide_item = models.CharField(max_length=32)