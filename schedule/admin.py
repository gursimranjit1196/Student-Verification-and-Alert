from django.contrib import admin

from .models import Timetable

# Register your models here.

class TimetableAdmin(admin.ModelAdmin) :
    class Meta :
        model=Timetable

admin.site.register(Timetable,TimetableAdmin)
