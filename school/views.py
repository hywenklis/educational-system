from django.shortcuts import render
from .models import Student, Course

def list_students(request):
    students = [
        Student(name="Maria", lastname="Silva", email="maria.silva@exemple.com"),
        Student(name="João", lastname="Souza", email="joao.souza@example.com"),
    ]
    return render(request, 'school/student.html', {'students': students})

def list_courses(request):
    courses =  [
        Course(title="Matemática", description="Curso de matemática básica"),
        Course(title="História", description="Curso de história geral"),
    ]
    return render(request, 'school/course.html', {'courses': courses})
