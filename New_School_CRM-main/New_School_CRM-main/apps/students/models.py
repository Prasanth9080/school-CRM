from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.corecode.models import StudentClass


class Student(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )
    registration_number = models.CharField(max_length=200, unique=True)
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_of_admission = models.DateField(default=timezone.now)

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    parent_mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )

    address = models.TextField(blank=True)
    others = models.TextField(blank=True)
    passport = models.ImageField(blank=True, upload_to="students/passports/")

    class Meta:
        ordering = ["surname", "firstname", "other_name"]

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.other_name} ({self.registration_number})"

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")




############## new model for student details

# students/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

class LeaveRequeststudent(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    standard = models.CharField(max_length=50)
    reason = models.TextField()
    date_applied = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.student.username} - {self.status}"


########### new models for student report card

# from django.db import models
# from django.contrib.auth.models import User
# from apps.corecode.models import StudentClass

# class StuReportCard(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE)
#     standard = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, null=True, blank=True)
    
#     tamil = models.PositiveIntegerField()
#     english = models.PositiveIntegerField()
#     maths = models.PositiveIntegerField()
#     science = models.PositiveIntegerField()
#     social = models.PositiveIntegerField()

#     status = models.CharField(max_length=10, choices=[("pass", "Pass"), ("fail", "Fail")])
#     comments = models.TextField(blank=True)
#     parent_signature = models.BooleanField(default=False)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student.username} - {self.standard}"



#### model for updated 

from django.db import models
from django.contrib.auth.models import User
from apps.corecode.models import StudentClass, AcademicSession
from ckeditor.fields import RichTextField

class StuReportCard(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    standard = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, null=True, blank=True)
    section = models.CharField(max_length=10, blank=True)
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.SET_NULL, null=True, blank=True)

    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    address = RichTextField(blank=True)
    admission_number = models.CharField(max_length=30, blank=True)
    roll_number = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    tamil = models.PositiveIntegerField()
    english = models.PositiveIntegerField()
    maths = models.PositiveIntegerField()
    science = models.PositiveIntegerField()
    social = models.PositiveIntegerField()

    overall_total = models.PositiveIntegerField(default=0)
    overall_percentage = models.FloatField(default=0.0)
    overall_grade = models.CharField(max_length=5, default="", blank=True)

    status = models.CharField(max_length=10, choices=[("pass", "Pass"), ("fail", "Fail")])
    term = models.CharField(max_length=10, choices=[("Term I", "Term I"), ("Term II", "Term II")], default="")
    comments = RichTextField(blank=True)

    date = models.CharField(max_length=50, blank=True)
    signature_class_teacher = models.CharField(max_length=100, blank=True)
    signature_principal = models.CharField(max_length=100, blank=True)
    parent_signature = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.standard} - {self.term}"


###### Attendance report card model


from django.db import models
from django.contrib.auth.models import User

ATTENDANCE_STATUS = (
    ('present', 'Present'),
    ('absent', 'Absent'),
    ('permission', 'Permission'),
)

DAYS = (
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
)

class AttendanceRecord(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=10, choices=DAYS)
    status = models.CharField(max_length=15, choices=ATTENDANCE_STATUS)
    message = models.TextField(blank=True)
    signature = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.student.username} - {self.date} - {self.status}"