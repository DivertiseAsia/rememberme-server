"""config URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from calendar_manager.views import HolidayViewSet, LeaveRequestViewSet, EventViewSet
from user_manager.views import AccountViewSet, PasswordViewSet

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet, basename='account')
router.register(r'password', PasswordViewSet, basename='password')
router.register(r'holiday', HolidayViewSet, basename='holiday')
router.register(r'leave', LeaveRequestViewSet, basename='leave')
router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-explorer/', get_swagger_view(title='RememberME API')),
    path('', include((router.urls, 'api'), namespace='v1')),
]
