from django.shortcuts import render,redirect
from app.models import CourseModel,StudentModel
from django.contrib import messages

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def addCourse(request):
    return render(request,"add_course.html")


def save_course(request):
    cid = request.POST.get('c1')
    cname = request.POST.get('c2')
    CourseModel(course_no=cid,course_name=cname).save()
    messages.success(request,"saved")
    return redirect('add_course')


def view_course(request):
    return render(request,"viewcourse.html",{"data":CourseModel.objects.all()})


def add_student(request):
    return render(request,"add_student.html",{"data":CourseModel.objects.all()})


def save_student(request):
    sno = request.POST.get('s1')
    sname = request.POST.get('s2')
    scno = request.POST.get('s3')
    subject = request.POST.getlist('s4')
    st = StudentModel(student_no=sno,student_name=sname,contact_no=scno)
    st.save()
    st.course.set(subject)
    return redirect('main')


def view_student(request):
    return render(request,"view_student.html",{"data":StudentModel.objects.all()})