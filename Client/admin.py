from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(enquery)
admin.site.register(review)