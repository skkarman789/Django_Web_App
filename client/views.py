from django.shortcuts import render, redirect,HttpResponse
from .forms import UserForm,UserTaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models  import UserTask
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from datetime import date
from django.core.mail import EmailMessage

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
                data=UserTask.objects.filter(date=date.today(),user=request.user).count()
                
                messages.success(request, "Login successful.")
                if data is not 0:
                    messages.success(request, "You have {} tasks today.".format(data))
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
    if not request.user.is_superuser:
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
    else:
        data = UserTask.objects.filter(date=date.today()).all()
        return render(request, "daily_task.html",{'data':data})

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

def remaindersender(request):
    data = UserTask.objects.filter(date=date.today()).all()
    email=[]
    phone=[]
    for i in data:
        if i.user.email is not None:
            email.append(i.user.email)
        if i.user.phone is not None:
            phone.append(i.user.phone)
    if request.method=="POST":
        msg = """
        <html>
        <body>
            <p>Hi User,</p>
            <p>I hope this message finds you well.</p>
            <p>This is just a friendly reminder that you have some tasks to complete today.</p>
            <p>It's always helpful to stay organized and ensure everything gets done on time.</p>
            <p>Please take a moment to review your task list for today and prioritize them accordingly.</p>
            <p>Remember, tackling tasks one at a time can help reduce stress and increase productivity.</p>
            <p>If you have any questions or need assistance with anything, feel free to reach out.</p>
            <p>I'm here to help!</p>
            <p>Best regards,<br>Orizzonte</p>
        </body>
        </html>
        """  
        email = EmailMessage('Reminder: Tasks to Complete Today', msg ,"arman.arbaz111@gmail.com",email)
        email.content_subtype = "html"
        email.send()
        error_msg="Email Sent"
        messages.error(request,(error_msg))
        return redirect('UserTasks')
         
    return redirect('UserTasks')

