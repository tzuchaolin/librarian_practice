from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf.urls import include
from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('catalog/', include('catalog.urls')),

    re_path('.*', views.index),
]
