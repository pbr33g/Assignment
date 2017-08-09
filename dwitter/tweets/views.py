from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import View, TemplateView
from django.contrib.auth.forms import UserCreationForm
import forms
from django.shortcuts import render
# Create your views here.

class MyDtwitter(TemplateView):
    def get(self, request):
        # return HttpResponse("sdf")
        # return render(request,'myApp/templateHTML.html')
        # form = forms.DweetsForm(initial={'message':'Write here'})
        form = forms.DweetsForm()
        return render(request, 'tweet.html', {'form':form})
        # return TemplateResponse(request, self.template_name)

    def post(self, request):
        print request.POST
        form = forms.DweetsForm(request.POST)
        if False and form.is_valid():
            cd = form.cleaned_data
            tweet_text = cd['tweet_text']
            return HttpResponseRedirect('/tweets')
        return render(request, 'tweet.html', {'form':form})