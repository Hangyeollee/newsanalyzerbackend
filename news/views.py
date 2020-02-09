# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SwedishWords
from .serializers import SwedishwordsSerializer
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Sum, Count
import json
class ListSwedishwordsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = SwedishWords.objects.filter(count__gte=50).order_by('-count')
    serializer_class = SwedishwordsSerializer


def all_word_api(request):

	words = SwedishWords.objects.filter(count__gte=50).order_by('-count')[:10:1]
	data = serializers.serialize('json', words)
	return HttpResponse(data, content_type='application/json; charset=utf-8')
	#return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii':False})

def top_ten(request):
	words = SwedishWords.objects.filter(count__gte=50).order_by('-count')[:10:1]
	data = serializers.serialize('json', words)
	return HttpResponse(data, content_type='application/json; charset=utf-8')

def all_word_count(request):
	words = SwedishWords.objects.values('word').annotate(count=Sum('count')).order_by('-count')[:10:1]
	print(words)
	#data = serializers.serialize('json', words)
	#return HttpResponse(data, content_type='application/json; charset=utf-8')
	#return JsonResponse(list(words), content_type='application/json; charset=utf-8', safe=False)
	#return JsonResponse(json.dumps(list(words), ensure_ascii=False), safe=False)
	return JsonResponse(words, safe=False, json_dumps_params={'ensure_ascii': False})