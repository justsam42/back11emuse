from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Text),
admin.site.register(Link),
admin.site.register(Media),
admin.site.register(Bloc),
admin.site.register(Section),
admin.site.register(Page)
