from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import logout

from models import Word

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
        
        context = {}
        return render(request, 'settings.html', context)


