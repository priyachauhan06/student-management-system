from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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

#@api_view(['POST'])
def signup(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Invalid Username or Password'
        })

    return render(request, 'login.html')


from django.contrib.auth import logout

def logout_view(request):

    logout(request)

    return redirect('login')