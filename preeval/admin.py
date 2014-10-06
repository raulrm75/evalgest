from django.contrib import admin
from preeval.models import (
    Level, Group, Student, Teacher, Subject, Mark, Remarks)

admin.site.register(Level)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Mark)
admin.site.register(Remarks)
