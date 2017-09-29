
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Course, City, Country


class CourseList(ListView):
    model = Course

'''
class TablaList(ListView):
    model = Tabla

class TablitaList(ListView):
    model = Tablita
'''


class CourseDetail(DetailView):
    model = Course

'''
class TablaDetail(DetailView):
    model = Tabla

class TablitaDetail(DetailView):
    model = Tablita
'''

class CourseCreation(CreateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['name', 'city', 'country']


class CourseUpdate(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['name', 'city', 'country']

'''
class TablaCreation(CreateView):
    model = Tabla
    success_url = reverse_lazy('courses:list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['ciudad']


class TablaUpdate(UpdateView):
    model = Tabla
    success_url = reverse_lazy('courses:list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['ciudad']

class TablitaCreation(CreateView):
    model = Tablita
    success_url = reverse_lazy('courses:list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['pais']


class TablitaUpdate(UpdateView):
    model = Tablita
    success_url = reverse_lazy('courses:list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['pais']
'''
class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')

'''
class TablaDelete(DeleteView):
    model = Tabla
    success_url = reverse_lazy('courses:list')

class TablitaDelete(DeleteView):
    model = Tablita
    success_url = reverse_lazy('courses:list')
'''