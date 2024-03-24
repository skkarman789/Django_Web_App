from django.urls import path
from  .views import home,login_view,signup,signout,about,services,scholarships,study_abroad,universities,UserTasks,Update,Delete,datefilter,remaindersender
urlpatterns = [
    path('',home,name='home'),
    path('login',login_view,name='login_view'),
    path('signup',signup,name='signup'),
    path('signout',signout,name='signout'),
    path('about',about,name='about'),
    path('scholarships',scholarships,name='scholarships'),
    path('services',services,name='services'),
    path('universities',universities,name='universities'),
    path('studyabroad',study_abroad,name='study_abroad'),
    path('tasks',UserTasks,name='UserTasks'),
    path('update/<int:pk>',Update ,name= 'update'),
    path('delete/<int:pk>',Delete ,name= 'delete'),
    path('datefilter',datefilter,name='datefilter'),
    path('remaindersender',remaindersender,name='remaindersender')
]



