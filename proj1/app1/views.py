from django.shortcuts import render
from .models import Employee

def dispview(request):
    obj = Employee.objects.all()
    temp_nm = 'home.html'
    context = {'obj':obj}
    return render(request,temp_nm,context)
