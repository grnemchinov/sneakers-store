from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import EmailMessage, EmailMultiAlternatives

from store.forms import FeedbackForm
from store.models import Sneakers, Feedback, WishList
from django.contrib import messages


def index(request):
    items = Sneakers.objects.all()
    context = {"items": items}
    return render(request, 'store/index.html', context=context)


def detail(request, item_id):
    item = Sneakers.objects.get(id=item_id)
    wishlist = WishList(request)
    in_wishlist = item_id in wishlist.items
    context = {"item": item, "in_wishlist": in_wishlist}
    return render(request, 'store/detail.html', context=context)


def services(request):
    return render(request, 'store/services.html')


def about(request):
    return render(request, 'store/about.html')


def contacts(request):
    return render(request, 'store/contacts.html')


def feedbacks(request):
    items = Feedback.objects.order_by('-id')[:3:-1]
    context = {"items": items}
    return render(request, 'store/feedbacks.html', context=context)


def feedback_detail(request, item_id):
    item = Feedback.objects.get(id=item_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(feedbacks)
    else:
        form = FeedbackForm(instance=item)
        context = {'form': form}
        return render(request, 'store/feedback_detail.html', context)


def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(feedbacks)
    else:
        form = FeedbackForm()
        context = {'form': form}
        return render(request, 'store/feedback_detail.html', context)


def feedback_delete(request, item_id):
    Feedback.objects.get(id=item_id).delete()
    return redirect(feedbacks)


def wishlist_add(request, item_id):
    wishlist = WishList(request)
    if item_id in wishlist.items:
        return wishlist_remove(request, item_id)
    wishlist.add(item_id)
    messages.success(request, "Success added!")
    return redirect(f'/detail/{item_id}')


def wishlist_remove(request, item_id):
    wishlist = WishList(request)
    wishlist.remove(item_id)
    messages.success(request, "Success removed!")
    return redirect(f'/detail/{item_id}')


def wishlist_list(request):
    wishlist = WishList(request)
    context = {"items": wishlist}
    return render(request, 'store/wishlist.html', context=context)


def wishlist_send(request):
    user = request.user
    wishlist = WishList(request)
    context = {"items": wishlist, "user": user}
    plaintext = get_template('email.txt')
    htmly = get_template('email.html')
    text_content = plaintext.render(context=context)
    html_content = htmly.render(context=context)
    email = EmailMultiAlternatives('New wishes!', text_content, to=['mnemchinov@mail.ru'])
    email.attach_alternative(html_content, "text/html")
    email.send()
    wishlist.clear()
    return render(request, 'store/index.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
