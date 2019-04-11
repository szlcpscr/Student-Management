from django.contrib import admin
from .models import Course, Program, Upload, State, Student, New, Grade, Exam_deadline, Exams, Profile, User_type


admin.site.register(Profile)
admin.site.register(User_type)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'file')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade', )

class RegisteredCourseAdmin(admin.ModelAdmin):
	list_display = ('user', 'program', 'course', 'registered', 'featured', )


admin.site.site_header = 'ABC University'
admin.site.register(Exams)
admin.site.register(Exam_deadline)
# admin.site.register(RegisteredCourse, RegisteredCourseAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(New)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Program)
admin.site.register(Upload, UploadAdmin)
admin.site.register(State)
