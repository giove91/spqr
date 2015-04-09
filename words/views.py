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

from models import Word, Keyword

import random


def logout_view(request):
    logout(request)
    return redirect('wordview')



class WordView(View):
    def get(self, request):    
        
        context = {}
        return render(request, 'word.html', context)



class GetWordView(View):
    def get(self, request):
        
        n = Word.objects.all().count()
        random_index = random.randint(0, n-1)
        word = Word.objects.all()[random_index]
        
        data = {
            'russian': word.russian,
            'italian': word.italian,
        }
        
        return JsonResponse(data)


class SettingsView(View):
    def get(self, request):    
        
        keywords = Keyword.objects.all()
        
        settings = request.session.get("settings", None)
        
        if settings is not None:
            chosen_keywords = [k for k in keywords if k.id in settings["chosen_keywords"]]
            filter_type = settings["filter_type"]
        else:
            chosen_keywords = []
            filter_type = "or"
        
        available_keywords = [k for k in keywords if k not in chosen_keywords]
        
        context = {
            'keywords': keywords,
            'available_keywords': available_keywords,
            'chosen_keywords': chosen_keywords,
            'filter_type': filter_type,
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
            
            return HttpResponse("OK")
        
        except Exception as E:
            print E
            return HttpResponse("Error")
    
    # FIXME: handle csrf
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(SaveSettingsView, self).dispatch(*args, **kwargs)


