from django.contrib import admin
from django.urls import path, include
from store.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index', index, name='index'),
    path('services', services, name='services'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('feedbacks', feedbacks, name='feedbacks'),
    path('feedback/create', feedback_create, name='feedback_create'),
    path('feedback/delete/<int:item_id>', feedback_delete,
         name='feedback_delete'),
    path('feedback/<int:item_id>', feedback_detail, name='feedback_detail'),
    path('detail/<int:item_id>', detail, name='detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('detail/wishlist/add/<int:item_id>', wishlist_add, name='wishlist_add'),
    path('detail/wishlist/remove/<int:item_id>', wishlist_remove, name='wishlist_remove'),
    path('wishlist', wishlist_list, name='wishlist_list'),
    path('wishlist/send', wishlist_send, name='wishlist_send'),
]
