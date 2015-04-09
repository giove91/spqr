from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.contrib.auth import logout

from django.db.models import Q

from models import Word, Keyword

import random


def get_settings(request):
    default_settings = {
        'chosen_keywords': [],
        'filter_type': "or",
    }
    return request.session.get("settings", default_settings)


def get_queryset(request):
    """
    Returns the queryset of words, according to the settings stored in the session.
    """
    settings = get_settings(request)
    
    if len(settings['chosen_keywords']) == 0:
        queryset = Word.objects.all()
    elif settings['filter_type'] == 'and':
        queryset = Word.objects.all()
        for k_id in settings['chosen_keywords']:
            queryset = queryset.filter(keywords__pk=k_id)
    elif settings['filter_type'] == 'or':
        q = Q()
        for k_id in settings['chosen_keywords']:
            q = q | Q(keywords__pk=k_id)
        queryset = Word.objects.filter(q)
    else:
        raise NotImplementedError
    
    return queryset


def logout_view(request):
    logout(request)
    return redirect('wordview')


class WordView(View):
    def get(self, request):    
        
        context = {}
        return render(request, 'word.html', context)



class GetWordView(View):
    def get(self, request):
        
        queryset = get_queryset(request)
        
        n = queryset.count()
        if n == 0:
            queryset = Word.objects.all()
            n = queryset.count()
        
        random_index = random.randint(0, n-1)
        word = queryset[random_index]
        
        data = {
            'russian': word.russian,
            'italian': word.italian,
        }
        
        return JsonResponse(data)


class SettingsView(View):
    def get(self, request):    
        
        keywords = Keyword.objects.all()
        
        settings = get_settings(request)
        count = get_queryset(request).count()
        
        chosen_keywords = [k for k in keywords if k.id in settings["chosen_keywords"]]
        filter_type = settings["filter_type"]
        
        available_keywords = [k for k in keywords if k not in chosen_keywords]
        
        context = {
            'keywords': keywords,
            'available_keywords': available_keywords,
            'chosen_keywords': chosen_keywords,
            'filter_type': filter_type,
            'no_words': count == 0,
        }
        return render(request, 'settings.html', context)


class SaveSettingsView(View):
    
    def post(self, request):
        try:
            data = request.POST
            chosen_keywords = [int(id) for id in request.POST.getlist('chosen_keywords[]')]
            filter_type = request.POST['filter_type']
            
            request.session["settings"] = {
                'chosen_keywords': chosen_keywords,
                'filter_type': filter_type,
            }
            
            queryset = get_queryset(request)
            return HttpResponse(queryset.count())
        
        except Exception as E:
            print E
            return HttpResponse("Error")
    
    # FIXME: handle csrf
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(SaveSettingsView, self).dispatch(*args, **kwargs)


