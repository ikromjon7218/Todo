from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginview),
    path('todo/', todo),
    path('todo_delete/<int:son>/', todo_delete),
    path('todo_edit/<int:son>/', todo_edit),


    path('logout/', logoutview),
    path('loginview/', loginview),
    path('register/', register),



]
