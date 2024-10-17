from django.shortcuts import render, redirect
from .forms import EnrollForm, Registration, LoginForm
from .models import Course, Student
from django.contrib.auth import login, logout, get_user_model, authenticate
from django.contrib import messages


# Create your views here.
def homepage(request):

    return render(request, 'index.html', {'courses': Course.objects.all()})

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course.html', {'course': course})


def enrollment(request):
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            course = form.cleaned_data.get('course')
            student.course.add(course)
            return redirect('homepage')
    else:
        form = EnrollForm()

    return render(request, 'enroll.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = Registration()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Muvafaqiyatli Login')
            return redirect('homepage')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def user_logout(request):
        logout(request)
        messages.success(request, 'Muvafaqiyatli Logout')
        return redirect('homepage')