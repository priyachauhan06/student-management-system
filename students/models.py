from django.db import models


class Student(models.Model):

    name = models.CharField(
        max_length=100,
        help_text="Enter student's full name"
    )

    roll_no = models.IntegerField()

    course = models.CharField(max_length=100)

    email = models.EmailField(
        help_text="Enter student's email"
    )

    phone = models.CharField(
        max_length=10,
        help_text="Enter 10-digit phone number"
    )

    class Meta:
        ordering = ["roll_no"]
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
    
    