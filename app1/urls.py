from django.urls import path
from app1.views.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
]