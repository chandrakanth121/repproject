from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,TemplateView
from testapp.models import test
from django.urls import reverse_lazy# Create your views here.



class testlist(ListView):
    model=test




class testdetail(DetailView):
    model=test

class testcreate(CreateView):
    model=test
    fields=('name','cross')
class testdelete(DeleteView):
    model=test
    success_url=reverse_lazy('home')
