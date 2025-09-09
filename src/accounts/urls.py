""" from django.urls import path
from . import views



urlpatterns = [
    # ...existing urls...
    path('profile/', views.profile_view, name='profile'),
]
 """