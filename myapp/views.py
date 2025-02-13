from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Faculty, Subject, Class, TimetableSlot
from .forms import FacultyForm, SubjectForm, ClassForm
from .geneticalgorithm import generate_timetable

def home(request):
    return render(request, "myapp/home.html")

def add_faculty(request):
    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FacultyForm()
    return render(request, "myapp/addfaculty.html", {"form": form})

def add_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubjectForm()
    return render(request, "myapp/addsubject.html", {"form": form})

def add_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClassForm()
    return render(request, "myapp/addclass.html", {"form": form})

def generate_timetable_view(request):
    if request.method == "POST":
        timetables = generate_timetable()
        return render(request, "myapp/timetable.html", {"timetables": timetables})
    return render(request, "myapp/timetable.html")
