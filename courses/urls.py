from django.conf.urls import url

from .views import (
    CourseList,
    CourseDetail,
    CourseCreation,
    CourseUpdate,
    CourseDelete,
    CountryList,
    CountryDetail,
    CountryCreation,
    CountryUpdate,
    CountryDelete,
    CityList,
    CityDetail,
    CityCreation,
    CityUpdate,
    CityDelete,
   
)

urlpatterns = [

    url(r'^$', CourseList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='detail'),
    url(r'^nuevo$', CourseCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name='delete'),

    url(r'^country/$', CountryList.as_view(), name='country_list'),
    url(r'^(?P<pk>\d+)$', CountryDetail.as_view(), name='country_detail'),
    url(r'^country/nuevo$', CountryCreation.as_view(), name='country_new'),
    url(r'^country/editar/(?P<pk>\d+)$', CountryUpdate.as_view(), name='country_edit'),
    url(r'^country/borrar/(?P<pk>\d+)$', CountryDelete.as_view(), name='country_delete'),

    url(r'^city/$', CityList.as_view(), name='city_list'),
    url(r'^(?P<pk>\d+)$', CityDetail.as_view(), name='city_detail'),
    url(r'^city/nuevo$', CityCreation.as_view(), name='city_new'),
    url(r'^city/editar/(?P<pk>\d+)$', CityUpdate.as_view(), name='city_edit'),
    url(r'^city/borrar/(?P<pk>\d+)$', CityDelete.as_view(), name='city_delete'),
   
]

