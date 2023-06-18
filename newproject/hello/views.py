from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from hello.models import Sneakers


def index(request):
    items = Sneakers.objects.all()
    context = {"items": items}
    return render(request, 'hello/index.html', context=context)


def detail(request, item_id):
    item = Sneakers.objects.get(id=item_id)
    context = {"item": item}
    return render(request, 'hello/detail.html', context=context)


def services(request):
    return render(request, 'hello/services.html')


def about(request):
    return render(request, 'hello/about.html')


def contacts(request):
    return render(request, 'hello/contacts.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

