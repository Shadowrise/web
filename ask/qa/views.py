from django.http import HttpResponse, Http404 
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question
from django.shortcuts import render

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        raise Http404
     
    if limit > 100:
        limit = 10
        
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404        
        
    paginator = Paginator(qs, limit)
    paginator.baseurl = '/question/'
    
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

def new(request):
    qs = Question.objects.new()
    page = paginate(request, qs)    
    data = {
        'questions': page.object_list,
        'page': page,
        'title': 'New questions',
    }
    return render(request, 'questions.html', data)

def popular(request):
    qs = Question.objects.popular()
    page = paginate(request, qs)    
    data = {
        'questions': page.object_list,
        'page': page,
        'title': 'Popular questions',
    }
    return render(request, 'questions.html', data)

def one(request, id):
    question = Question.objects.get(id=id)
    data = {
        'question': question,
    }
    return render(request, 'question.html', data)

