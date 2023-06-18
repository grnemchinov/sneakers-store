from django.contrib import admin
from django.urls import path, include
from hello.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index', index, name='index'),
    path('services', services, name='services'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('detail/<int:item_id>', detail, name='detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
]
