from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Subject, Grade
from .forms import StudentForm, SubjectForm, GradeForm

def index(request):
    return render(request, 'performance_tracker/index.html')

def students(request):
    students = Student.objects.all()
    return render(request, 'performance_tracker/students.html', {'students': students})

def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'performance_tracker/subjects.html', {'subjects': subjects})

def grades(request):
    grades = Grade.objects.all()
    return render(request, 'performance_tracker/grades.html', {'grades': grades})

def report(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    best_student = max(students, key=lambda student: student.grade_set.aggregate(models.Avg('grade'))['grade__avg'])
    worst_student = min(students, key=lambda student: student.grade_set.aggregate(models.Avg('grade'))['grade__avg'])
    average_grades = {subject: subject.grade_set.aggregate(models.Avg('grade'))['grade__avg'] for subject in subjects}
    return render(request, 'performance_tracker/report.html', {
        'best_student': best_student,
        'worst_student': worst_student,
        'average_grades': average_grades
    })

