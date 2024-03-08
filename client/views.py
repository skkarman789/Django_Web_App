from django.shortcuts import render, redirect
from .forms import UserForm,UserTaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models  import UserTask
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404

def home(request):
    if request.user.is_authenticated:
            return render(request, "index.html") 
    else :
        error_msg="Login Required To Access The Page"
        messages.error(request,(error_msg))
    return redirect('login_view')


def login_view(request):
    if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password.")
    return render(request, "signin.html")

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.last_login=timezone.now()
            print("After setting last_login:", instance.last_login) 
            instance.save()
            error_msg="sign up Sucessful"
            messages.success(request,(error_msg))
            return redirect('login_view')
        else:
            error_msg="invalid details or password does not match"
            messages.error(request,(error_msg))
    else:
        form = UserForm()
    return render(request, "signup.html", {'form': form})

@login_required
def signout(request):
    logout(request)
    error_msg="logout Sucessful"
    messages.success(request,(error_msg))
    return redirect('login_view')

@login_required
def UserTasks(request):
    Status=""
    if request.method =='POST':
        form = UserTaskForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            if instance.status==True:
                Status="Completed"
            else:
                Status="Pending"
            instance.user=request.user
            instance.save()
            error_msg="Task Added Sucessfully"
            messages.success(request,(error_msg))
            return redirect('UserTasks')
    else:
        form = UserTaskForm()
    data=UserTask.objects.filter(user=request.user).order_by("-created_date")[:10]
    return render(request, "daily_task.html", {'form': form ,'data':data ,'Status':Status })

@login_required
def datefilter(request):
    if request.method == "POST":
        date = request.POST.get('date')
        data = UserTask.objects.filter(date=date,user=request.user)
        if not data:
            messages.success(request,("No Tasks Available This Date"))
        return render(request, "daily_task.html", {'data': data})
    else:
        return messages.success(request,"Date input field is empty")

     
@login_required
def Update(request, pk):
    instance = get_object_or_404(UserTask,id=pk)
    form = UserTaskForm(instance=instance)
    Status = ""
    if request.method == "POST":
        form = UserTaskForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.status:
                Status = "Completed"
            else:
                Status = "Pending"
            instance.user = request.user
            instance.save()
            error_msg="Task Updated Sucessfully"
            messages.success(request,(error_msg))
            return redirect('UserTasks')
    return render(request, "daily_task.html", {'form': form, 'data': [instance],'instance':instance, 'Status': Status})


@login_required
def Delete(request, pk):
    instance = get_object_or_404(UserTask, id=pk)
    instance.delete()
    print(instance)
    messages.success(request, "Task deleted successfully.")
    return redirect('UserTasks')
          

def about(request):
    if request.user.is_authenticated:
            return render(request, "about.html") 
    else :
        error_msg="Login Required To Access The Page"
        messages.error(request,(error_msg))
    return redirect('login_view')

def services(request):
    if request.user.is_authenticated:
            return render(request, "services.html") 
    else :
        error_msg="Login Required To Access The Page"
        messages.error(request,(error_msg))
    return redirect('login_view')

def study_abroad(request):
    if request.user.is_authenticated:
            return render(request, "study_abroad.html") 
    else :
        error_msg="Login Required To Access The Page"
        messages.error(request,(error_msg))
    return redirect('login_view')

def universities(request):
    if request.user.is_authenticated:
            return render(request, "universities.html") 
    else :
        error_msg="Login Required To Access The Page"
        messages.error(request,(error_msg))
    return redirect('login_view')

def scholarships(request):    
    if request.user.is_authenticated:
            return render(request, "scholarships.html") 
    else :
        error_msg="Login Required To Access The Page"
        messages.error(request,(error_msg))
    return redirect('login_view')


