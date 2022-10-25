from django.contrib import admin

from articles.models import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Article)