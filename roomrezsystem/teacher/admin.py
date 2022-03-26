from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    list_display = ('id', 'realname', 'tel','role','cardid')