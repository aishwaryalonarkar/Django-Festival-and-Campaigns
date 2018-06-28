from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import admin
from .models import festmodel
from .models import campaign
from .forms import NameForm
from django.contrib import admin
'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")'''

def index(request):
    template_name = 'festivalapp/index.html'
    return render(request,template_name)

def main(request):
    template_name = 'festivalapp/index.html'
    return render(request,template_name)

def flist(request):
    fest1 = festmodel.objects.all() 
    template_name = 'festivalapp/fest1.html'
    context_object_name = {'festmodel':fest1}
    return render(request,template_name,context_object_name)

def finfo(request,fest_id):
    fest1 = festmodel.objects.get(id=fest_id)
    template_name = 'festivalapp/fest2.html'
    context_object_name = {'festmodel':fest1}
    return render(request,template_name,context_object_name)

def fest_campaign(request,pk):
    camp1 = campaign.objects.get(id=pk)
    template_name = 'festivalapp/event.html'
    context_object_name = {'campaign':camp1}
    return render(request,template_name,context_object_name)

def fsearched(request,id):
    #fest1 = festmodel.objects.filter(args=(festmodel.id)) 
    fest1 = get_object_or_404(festmodel, pk=month)
    try:
        obj_entered = festmodel.obj_set.get(pk=request.POST['obj'])
    except (KeyError,obj.DoesNotExist):
    	return render(request, 'festivalapp/fest3.html', {
            'festmodel': fest1,
            'error_message': "You didn't enter a anything.",
        })
    else:
        return HttpResponseRedirect(reverse(args=(festmodel.id,)))


def elist(request):
    event1 = campaign.objects.all() 
    template_name = 'festivalapp/event1.html'
    context_object_name = {'campaign':event1}
    return render(request,template_name,context_object_name)

def einfo(request,pk):
    event1 = campaign.objects.get(id=pk) 
    template_name = 'festivalapp/event2.html'
    context_object_name = {'campaign':event1}
    return render(request,template_name,context_object_name)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'fest3.html', {'form': form})

    



