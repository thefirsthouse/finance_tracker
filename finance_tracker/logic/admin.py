from django.contrib import admin

from .models import Account, Transfer, Category, Record

admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Category)
admin.site.register(Record)
