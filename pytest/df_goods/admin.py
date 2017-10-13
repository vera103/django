from django.contrib import admin
from df_goods.models import *

# Register your models here.SS

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
class GoodInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gunit','gclick','gjianjie','gkucun','gcontent']


admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodInfoAdmin)


