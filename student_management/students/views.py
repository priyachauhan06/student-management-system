from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def home(request):
    students = Student.objects.all()

    return render(request, 'home.html', {
        'students': students
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect('home')


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.roll_no = request.POST['roll_no']
        student.course = request.POST['course']
        student.email = request.POST['email']
        student.phone = request.POST['phone']

        student.save()
        return redirect('home')

    return render(request, 'edit.html', {'student': student})