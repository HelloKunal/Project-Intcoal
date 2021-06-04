from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(tasks)
admin.site.register(thoughts)
admin.site.register(habits)
