from django.db import models

class CourseModel(models.Model):
    course_no = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=30)

class StudentModel(models.Model):
    student_no = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    course = models.ManyToManyField(CourseModel)
