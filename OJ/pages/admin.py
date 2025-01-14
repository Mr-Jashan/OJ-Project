from django.contrib import admin
# from pages.models import question_list
from pages.models import *
# Register your models here.

admin.site.register(question_list)
admin.site.register(testcase)
admin.site.register(code_record)
admin.site.register(code_check)

# class CodeRecordAdmin(admin.ModelAdmin):
#     list_display = ('username', 'language', 'code', 'created_at')

# admin.site.register(code_record, CodeRecordAdmin)

