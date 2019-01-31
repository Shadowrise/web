from django.http import HttpResponse, Http404 
from django.core.paginator import Paginator
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
        'paginator': paginator,
        'page': page,
    }
    return render(request, 'qa/new.html', data)

def popular(request):
    return HttpResponse('')

def one(request, question_id):
    return HttpResponse('')

