
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
    path("profiles/", include('profiles.urls')),
    
]


    