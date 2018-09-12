from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import FeedbackForm
# Create your views here.

def index(request):
    return render(request, 'flatpages/index.html')

def about_us(request):
    return render(request, 'flatpages/about_us.html')

def faq(request):
    return render(request, 'flatpages/faq.html')

def contacts(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail('Сообщение от {}'.format(cd['name']),
                        'Email отправителя: {}\nТекст письма: {}'.format(cd['email'],cd['message']),
                        'Mell1990ad@gmail.com',
                        ['kornilovguki@yandex.ru'])
    else:
        form = FeedbackForm()
    return render(request, 'flatpages/contacts.html', {'form':form})

def feedback(request):
    return HttpResponse('feedback')

def opt(request):
    return render(request, 'flatpages/opt.html')
