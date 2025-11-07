from django.shortcuts import render
from . import models

# Create your views here.
def student_list(request):
    students = models.Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    pass