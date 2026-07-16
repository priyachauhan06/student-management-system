from .models import Student


def dashboard_callback(request, context):
    context["student_count"] = Student.objects.count()
    context["course_count"] = Student.objects.values("course").distinct().count()

    return context