from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Student


@admin.register(Student)
class StudentAdmin(ModelAdmin):

    actions = ["delete_selected"]

    list_display = (
        "roll_no",
        "name",
        "course",
        "email",
        "phone",
    )

    search_fields = (
        "name",
        "roll_no",
        "course",
        "email",
    )

    list_filter = (
        "course",
    )

    ordering = ("roll_no",)

    list_per_page = 10

    fieldsets = (
    ("👨‍🎓 Student Information", {
        "fields": ("name", "roll_no")
    }),

    ("📚 Course Information", {
        "fields": ("course",)
    }),

    ("📞 Contact Information", {
        "fields": ("email", "phone")
    }),
)