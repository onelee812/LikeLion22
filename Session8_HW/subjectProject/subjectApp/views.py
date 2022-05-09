from django.shortcuts import render, redirect
from subjectApp.forms import SubjectModelForm
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy


class AddMajorView(CreateView):
    model=Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

class AddSubjectView(CreateView):
    model=Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

def home(request):
    subjects = Subject.objects.all()
    majors = Major.objects.all()
    return render(request, 'home.html', {'subjects' : subjects, 'majors' : majors})
    
def computerSubjectView(request):
    subjects = Subject.objects.all()
    computerMajor = subjects.filter(major__title='컴퓨터학과')
    return render(request, 'computer.html', {'computerMajor': computerMajor})


class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')

class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')

def DeleteMajorView(request, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    delMajor.delete()
    return redirect('home')

# Create your views here.
