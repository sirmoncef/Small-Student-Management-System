from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def addshow(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('addshow')
    else:
        form = StudentForm()
    
    info = Student.objects.all()
    return render(request, 'Student/addshow.html', {'form': form, 'info': info})

def delete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.delete()
    return redirect('addshow')

def modify(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('addshow')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'Student/modify.html', {'form': form, 'student_id': pk})  
