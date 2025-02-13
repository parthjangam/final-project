import random
from .models import Faculty, Subject, Class, TimetableSlot

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
TIME_SLOTS = ["09:00", "10:00", "11:00", "12:00", "02:00", "03:00", "04:00"]

def is_valid_schedule(timetable):
    faculty_timing = {}
    class_timing = {}

    for slot in timetable:
        faculty_key = (slot['faculty'], slot['day'], slot['time_slot'])
        class_key = (slot['class_info'], slot['day'], slot['time_slot'])

        if faculty_key in faculty_timing or class_key in class_timing:
            return False  # Conflict detected

        faculty_timing[faculty_key] = True
        class_timing[class_key] = True

    return True

def generate_timetable():
    timetable = []
    all_classes = Class.objects.all()
    all_subjects = Subject.objects.all()

    for class_info in all_classes:
        for subject in all_subjects.filter(class_info__year=class_info.year):
            faculty_list = list(subject.faculty.all())
            if not faculty_list:
                continue

            faculty = random.choice(faculty_list)
            day = random.choice(DAYS)
            time_slot = random.choice(TIME_SLOTS)

            timetable.append({
                "class_info": class_info,
                "subject": subject,
                "faculty": faculty,
                "day": day,
                "time_slot": time_slot
            })

            if not is_valid_schedule(timetable):
                timetable.pop()  # Remove invalid entry and retry

    return timetable
