"""
URL configuration for cfehome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .view import home_page_view, pw_protected_view, user_only_view,staff_only_view
from accounts import views as auth_views


#đường dẫn chính 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view),
    path('register/', auth_views.register_view),   # vẫn giữ nếu muốn custom register
    path('accounts/', include('allauth.urls')),    # allauth + allauth_ui sẽ lo login/logout
    path("protected/",pw_protected_view ), # pw_protected_view là hàm view
    path("protected/user-only", user_only_view), # user_only_view là hàm view
    path("protected/staff-only", staff_only_view),
]


    