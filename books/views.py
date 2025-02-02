from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
    return HttpResponse("Это страница обо мне.")

def text_and_photo(request):
    context = {
        'text': 'Это пример текста и фотографии.',
        'photo_url': 'https://via.placeholder.com/300',
    }
    return render(request, 'books/text_and_photo.html', context)

def system_time(request):
    now = datetime.now()
    return HttpResponse(f"Текущее время: {now}")
