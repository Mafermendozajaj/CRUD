
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


#Cursos
class CourseList(ListView):
    model = Course

class CourseDetail(DetailView):
    model = Course

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

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')



#Ciudad
class CityList(ListView):
    model = City

class CityDetail(DetailView):
    model = City

class CityCreation(CreateView):
    model = City
    success_url = reverse_lazy('courses:city_list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['ciudad']

class CityUpdate(UpdateView):
    model = City
    success_url = reverse_lazy('courses:city_list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['ciudad']

class CityDelete(DeleteView):
    model = City
    success_url = reverse_lazy('courses:city_list')


#Pais
class CountryList(ListView):
    model = Country

class CountryDetail(DetailView):
    model = Country

class CountryCreation(CreateView):
    model = Country
    success_url = reverse_lazy('courses:country_list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['pais']

class CountryUpdate(UpdateView):
    model = Country
    success_url = reverse_lazy('courses:country_list')
    #fields = ['name', 'start_date', 'end_date', 'picture']
    fields = ['pais']

class CountryDelete(DeleteView):
    model = Country
    success_url = reverse_lazy('courses:country_list')