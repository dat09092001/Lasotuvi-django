from django.urls import path
from lasotuvi.views import lasotuvi_django_index,api,upload_laso
urlpatterns = [
       path('',lasotuvi_django_index),
       path(r'api',api),
        path(r'upload_laso', upload_laso,),
]