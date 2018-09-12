from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm
# Create your views here.

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Feedback.objects.create(name=cd['name'], email=cd['email'], message=cd['message'])
    else:
        form = FeedbackForm()
    messages = Feedback.objects.filter(published=True)
    return render(request, 'feedback/feedback.html', {'messages': messages,
                                                          'form':form})
