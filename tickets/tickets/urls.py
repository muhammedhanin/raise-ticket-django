"""
URL configuration for ticket_raiser project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from core.views import ticket_list
from core.views import ticket_details
from rest_framework_simplejwt.views import(TokenObtainPairView , TokenRefreshView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ticket/" , ticket_list),
    path("ticket/<int:id>/" , ticket_details),
    path("api/token/",TokenObtainPairView.as_view()),        #this is for login
    path("api/Token/refresh/" , TokenRefreshView.as_view()),       #this is for get new token
]