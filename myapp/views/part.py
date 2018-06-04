from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Part
from django.utils.datastructures import MultiValueDictKeyError


def view(request):
	parts = Part.objects.all()
	return render(request, 'home.html', {'parts': parts})