from django.shortcuts import render
from django.http import HttpResponse
from . models import JSS1,JSS2,JSS3
from django.template import loader

def main(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request = request))

def jss1(request):
    model = JSS1.objects.all().values()
    template = loader.get_template('js1.html')
    context = {'js1':model}
    return HttpResponse(template.render(request = request, context = context))

def djss1(request, id):
    model = JSS1.objects.get(id = id)
    template = loader.get_template('djs1.html')
    context = {'djs1':model}
    return HttpResponse(template.render(request = request, context = context))

def jss2(request):
    model = JSS2.objects.all().values()
    template = loader.get_template('js2.html')
    context = {'js2':model}
    return HttpResponse(template.render(request = request, context = context))

def djss2(request, id):
    model = JSS2.objects.get(id = id)
    template = loader.get_template('djs2.html')
    context = {'djs2':model}
    return HttpResponse(template.render(request = request, context = context))

def jss3(request):
    model = JSS3.objects.all().values()
    template = loader.get_template('js3.html')
    context = {'js3':model}
    return HttpResponse(template.render(request = request, context = context))

def djss3(request, id):
    model = JSS3.objects.get(id = id)
    template = loader.get_template('djs3.html')
    context = {'djs3':model}
    return HttpResponse(template.render(request = request, context = context))