"""
URL configuration for cacvsa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from restapi.users.views import *
# from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    # path('', include_docs_urls(title='CACVSA API'), name='home'),
    path('', include('restapi.docs.urls'), name='docs'),
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/routes/', include('restapi.routes.urls'), name='routes'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
    path('login/', LoginViewSet.as_view()),
    path('logout/', LogoutViewSet.as_view())
]
