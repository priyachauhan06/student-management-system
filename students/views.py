from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

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

#@api_view(['POST'])
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

        return render(request, 'login.html')

    return render(request, 'login.html')

#@api_view(['POST'])
def logout_view(request):

    logout(request)

    return redirect('login')

@api_view(['POST'])
def signup_api(request):

    User.objects.create_user(
        username=request.data.get('username'),
        email=request.data.get('email'),
        password=request.data.get('password')
    )

    return Response({
        "message": "User registered successfully"
    })


@api_view(['POST'])
def login_api(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user:
        login(request, user)

        return Response({
            "message": "Login successful"
        })

    return Response({
        "error": "Invalid username or password"
    })


@api_view(['POST'])
def logout_api(request):

    logout(request)

    return Response({
        "message": "Logout successful"
    })