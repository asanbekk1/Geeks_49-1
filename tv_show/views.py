from django.shortcuts import render
from django.http import HttpResponse

def emodji(request):
    if request.method == 'GET':
        return HttpResponse('😛 😁 😉')

def text(request):
    if request.method == 'GET':
        return HttpResponse('Lorem ipsum dolor sit amet')

def image(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Hello</h1>'
                            'https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg?cs=srgb&dl=pexels-eberhardgross-1612351.jpg&fm=jpg')
