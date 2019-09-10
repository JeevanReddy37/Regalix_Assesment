"""Todo_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path

from TaskApp.views import view_home, view_task_details, view_register, view_delete, view_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', view_home),
    path('taskdetails/', view_task_details),
    path('addtask/', view_register),
    url(r'^delete/(?P<pid>[\d-]+)/$', view_delete),
    url(r'^update/(?P<pid>[\d-]+)/$', view_update),

    url(r'api/',include('TaskApp.rest_urls'))
]
