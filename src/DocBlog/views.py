from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    date =datetime.today()
    print(date)
    return render(request, 'DocBlog/index.html', context={'date': date})