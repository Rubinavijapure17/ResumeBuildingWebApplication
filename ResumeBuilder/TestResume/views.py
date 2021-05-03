from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView, UpdateView
from TestResume.models import Resume
from django.urls import reverse_lazy


# Create your views here.
class HomeData(TemplateView):
    template_name = 'TestResume\home.html'

class ReadData(ListView):
    model=Resume

class ReadCompleteData(ListView):
    model=Resume

class ReadOneData(DetailView):
    model=Resume

class InsertData(CreateView):
    model=Resume
    fields=('Name','Address','Phone_No','Emailid', 'SSC','HSC','UG','PG', 'Skills', 'Languages', 
    'Certificates', 'Projects', 'Experience','Summary')


class UpdateData(UpdateView):
    model=Resume
    fields=('Name','Address','Phone_No','Emailid', 'SSC','HSC','UG','PG', 'Skills', 'Languages', 
    'Certificates', 'Projects', 'Experience','Summary')



class DeleteData(DeleteView):
    model=Resume
    success_url=reverse_lazy('list')