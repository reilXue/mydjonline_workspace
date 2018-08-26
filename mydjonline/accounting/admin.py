from django.contrib import admin
from accounting.models import Agency_t,Settlement_t,Application_t,Tourist_t,Line_Price_t,Ref_Price_t
# Register your models here.
admin.site.register(Agency_t)
admin.site.register(Settlement_t)
admin.site.register(Application_t)
admin.site.register(Tourist_t)
admin.site.register(Line_Price_t)
admin.site.register(Ref_Price_t)