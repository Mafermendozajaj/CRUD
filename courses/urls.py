from django.conf.urls import url

from .views import (
    CourseList,
    CourseDetail,
    CourseCreation,
    CourseUpdate,
    CourseDelete,
   
)

urlpatterns = [

    url(r'^$', CourseList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='detail'),
    url(r'^nuevo$', CourseCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name='delete'),

   
]



'''

 TablaList,
    TablaDetail,
    TablaCreation,
    TablaUpdate,
    TablaDelete,
    TablitaList,
    TablitaDetail,
    TablitaCreation,
    TablitaUpdate,
    TablitaDelete



 url(r'^country/$', CountryList.as_view(), name='country_list'),
 

    url(r'^(?P<pk>\d+)$', TablaDetail.as_view(), name='detail'),
    url(r'^country/nuevo$', TablaCreation.as_view(), name='new'),
    url(r'^country/editar/(?P<pk>\d+)$', TablaUpdate.as_view(), name='edit'),
    url(r'^country/borrar/(?P<pk>\d+)$', TablaDelete.as_view(), name='delete'),

    url(r'^$', TablitaList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', TablitaDetail.as_view(), name='detail'),
    url(r'^nuevo$', TablitaCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', TablitaUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', TablitaDelete.as_view(), name='delete'),

'''