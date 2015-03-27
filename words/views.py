from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from models import Word

import random


class WordView(View):
    def get(self, request):    
        
        n = Word.objects.all().count()
        random_index = random.randint(0, n-1)
        word = Word.objects.all()[random_index]
        
        context = {'word': word}
        
        return render_to_response('word.html', context)



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

