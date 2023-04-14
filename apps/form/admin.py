from django.contrib import admin
from .models import Form, FormHistory


admin.site.register(Form)
admin.site.register(FormHistory)