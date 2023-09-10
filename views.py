from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .form import std
from .models import Projects, Students

def index(request):
    return render(request, 'crud/index.html')

def show(request):
    if request.method == 'GET':
        students_list = Students.objects.all().order_by('std_name')
    else:
        students_list = Students.objects.filter(std_name__startswith = request.POST['text'] )
    return render(request, 'crud/show.html', {'students_list': students_list})

def add(request,id=0):
    if request.method == 'GET': # if land by clicking add button
        if id==0:
            form = std()
            return render(request, 'crud/addData.html', {'form':form})
        else: # from update link
            students = Students.objects.get(pk=id)
            form = std(instance=students)
            return render(request, 'crud/addData.html', {'form': form})
    else : # when method == post
        if id == 0:
            form = std(request.POST)
            if form.is_valid():
                form.save()
            return redirect('../show')
        else: # for update in database
            students = Students.objects.get(pk=id)
            form = std(request.POST, instance=students)
            if form.is_valid():
                form.save()
            return redirect('../show')

def delete(request, id):
    students = Students.objects.get(pk=id)
    students.delete()
    return redirect('../../show')