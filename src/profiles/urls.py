

from django.urls import path, include

from .views import profile_view

#đường dẫn chính 
urlpatterns = [
    # <username>/ đây là tên biến động, có thể là bất cứ tên nào nhưng phải trùng với tên biến trong hàm view profile_view
    path("<str:username>/",profile_view),
]


    