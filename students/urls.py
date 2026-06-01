from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
