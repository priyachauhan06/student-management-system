from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
import requests

def home(request):
    
    response = requests.get(
        'http://127.0.0.1:8001/api/students/'
    )

    students = response.json()

    return render(request, 'home.html', {
        'students': students
    })


def delete_student(request, id):
    requests.delete(
        f'http://127.0.0.1:8001/api/students/{id}/'
    )

    return redirect('home')


def edit_student(request, id):

    if request.method == 'POST':

        data = {
            'name': request.POST['name'],
            'roll_no': request.POST['roll_no'],
            'course': request.POST['course'],
            'email': request.POST['email'],
            'phone': request.POST['phone']
        }

        requests.put(
            f'http://127.0.0.1:8001/api/students/{id}/',
            json=data
        )

        return redirect('home')

    response = requests.get(
        f'http://127.0.0.1:8001/api/students/{id}/'
    )

    student = response.json()

    return render(request, 'edit.html', {
        'student': student
    })

#@api_view(['POST'])
def signup(request):

    if request.method == 'POST':

        data = {
            'username': request.POST['username'],
            'email': request.POST['email'],
            'password': request.POST['password']
        }

        response = requests.post(
            'http://127.0.0.1:8001/api/signup/',
            json=data
        )

        if response.status_code == 200:
            return redirect('login')

    return render(request, 'signup.html')

#@api_view(['POST'])
def login_view(request):

    if request.method == 'POST':

        data = {
            'username': request.POST['username'],
            'password': request.POST['password']
        }

        response = requests.post(
            'http://127.0.0.1:8001/api/login/',
            json=data
        )

        if response.status_code == 200:
            return redirect('home')

    return render(request, 'login.html')

#@api_view(['POST'])
def logout_view(request):

    requests.post(
        'http://127.0.0.1:8001/api/logout/'
    )

    return redirect('login')

