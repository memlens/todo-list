from django.shortcuts import redirect, render
from todo.forms import CreateUserForm, LoginUserForm, TaskForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from todo.models import Task


#the home page view
def home(request):
    return render(request, 'todo/index.html')



#the register view
def register(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context={'form':form}
    return render(request, 'todo/register.html', context=context)


#the login view
def login_view(request):
    form=LoginUserForm()
    if request.method == 'POST':
        form=LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                #messages.success(request, "Loged in succesfully")
                return redirect('tasks')
    
    context={'form':form}
    return render(request, 'todo/login.html', context=context)



#the logout view
@login_required(login_url='login/')
def logout_view(request):
    auth.logout(request)
    return redirect('login')


#the tasks view
@login_required(login_url='login/')
def tasks_view(request):
    tasks=Task.objects.all()
    return render(request, 'todo/tasks.html', {'tasks':tasks})




#the create task view
@login_required(login_url='login/')
def create_task(request):
    form=TaskForm()
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    context={'form':form}
    return render(request, 'todo/create_task.html', context=context)



#the detail view
@login_required(login_url='login/')
def detail_view(request, pk):
    task=Task.objects.get(id=pk)
    return render(request, 'todo/detail.html', {'task':task})


#the update view
@login_required(login_url='login/')
def update_task(request, pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method == 'POST':
        form=TaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    context={'form':form}
    return render(request, 'todo/update_task.html', context=context)


#the delete view
@login_required(login_url='login/')
def delete_view(request, pk):
    task=Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'todo/delete_task.html', {'task':task})