"""
URL configuration for jspider project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from java.views import *
from python1.views import *
import sql1,webtechnology  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ravi/',ravi,name='ravi'),
    path('harshad/',harshad,name='harshad'),
    path('pranay/',pranay,name='pranay'),
    path('bharath/',bharath,name='bharath'),
    path('sql1/',include('sql1.urls')),
    path('webtechnology/',include('webtechnology.urls')),
    
]