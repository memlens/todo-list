from django.urls import path
from todo import views

urlpatterns = [
    path("", views.home, name="home"),
    
    path("register/", views.register, name='register'),
    
    path("login/", views.login_view, name="login"),
    
    path("logout/", views.logout_view, name="logout"),
    
    path("tasks/", views.tasks_view, name="tasks"),

    path("task/create/", views.create_task, name="create-task"),

    path("task/update/<int:pk>/", views.update_task, name="update-task"),

    path("task/delete/<int:pk>/", views.delete_view, name="delete-task"),

    path("task/<int:pk>/", views.detail_view, name='task-detail')
]