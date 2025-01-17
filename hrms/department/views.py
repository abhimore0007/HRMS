from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm
from django.contrib import messages 
# Create your views here.


def dashboard(request):
    departments = Department.objects.filter(status=True) 
    return render(request, 'core/home.html', {'departments': departments})


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added successfully.')
            return redirect('dashboard')
    else:
        form = DepartmentForm()
    return render(request, 'core/add_depatment.html', {'form': form})


def delete_department(request, id):
    department = get_object_or_404(Department, pk=id)

    if request.method == 'POST':
        department.status = False  
        department.save()
        return redirect('dashboard')

    return render(request, 'core/confirm_delete.html', {'department': department})

def update_department(request, id):
    department = get_object_or_404(Department, pk=id)
    form = DepartmentForm(request.POST or None, instance=department)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'core/update.html', {'form': form})

