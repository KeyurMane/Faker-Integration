from django.urls import path
from .views import dispview

urlpatterns = [
    path('disp/',dispview)
]