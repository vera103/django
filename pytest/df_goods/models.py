from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    isDeleted=models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode("utf-8")


class GoodsInfo(models.Model):
    gtitle=models.CharField(max_length=20)
    gpic=models.ImageField(upload_to='df_goods')
    gprice=models.DecimalField(max_digits=5,decimal_places=2)
    isDeleted = models.BooleanField(default=False)
    gunit=models.CharField(max_length=20)
    gclick=models.IntegerField()
    gjianjie=models.CharField(max_length=200)
    gkucun=models.IntegerField()
    gcontent= HTMLField()
    gtype=models.ForeignKey(TypeInfo)






