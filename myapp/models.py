from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.unique_id})"
    

#class Meta:
 #   app_label = "myapp" 

class Subject(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=[('Lecture', 'Lecture'), ('Lab', 'Lab')])
    faculty = models.ManyToManyField(Faculty)

    def __str__(self):
        return self.name

class Class(models.Model):
    year = models.IntegerField()  # e.g., 1st Year, 2nd Year
    division = models.CharField(max_length=10)  # e.g., A, B, C

    def __str__(self):
        return f"Year {self.year} - Division {self.division}"

class TimetableSlot(models.Model):
    class_info = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'),
                                                   ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
                                                   ('Friday', 'Friday'), ('Saturday', 'Saturday')])
    time_slot = models.TimeField()

    def __str__(self):
        return f"{self.class_info} - {self.subject} ({self.faculty}) on {self.day} at {self.time_slot}"
