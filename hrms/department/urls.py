from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/',views.register, name="register"),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('add/', views.add_department, name='add_department'),
    path('update/<int:id>/', views.update_department, name='update_department'),
    path('delete/<int:id>/', views.delete_department, name='delete_department'),
]
