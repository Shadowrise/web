from django.http import HttpResponse, Http404, HttpResponseRedirect 
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, m_signup, m_login, LoginResult
from qa.forms import AskForm, AnswerForm
from django.shortcuts import render
from datetime import datetime, timedelta

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
    paginator.baseurl = '/?page='
    
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
    
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_form.save()            
            return HttpResponseRedirect(question.get_url())
    else:
        answer_form = AnswerForm({'question': id})
        
    data = {
        'question': question,
        'answer_form': answer_form
    }
    return render(request, 'question.html', data)

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', { 'form': form })

def signup(request):
    error = ''
    username = ''
    email = ''
    password = ''
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        result = m_signup(username, email, password)
        if result.success:
            response = HttpResponseRedirect('/')
            #response.set_cookie('sessid', result.sessid, expires = datetime.now() + timedelta(days=1))
            return response
        else:
            error = result.err_msg
    return render(request, 'signup.html', {'error' : error, 'username' : username, 'email' : email, 'password' : password})

def login(request):
    error = ''
    username = ''
    password = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        result = m_login(username, password)
        if result.success:
            response = HttpResponseRedirect('/')
            response.set_cookie('sessid', result.sessid, expires = datetime.now() + timedelta(days=1))
            return response
        else:
            error = result.err_msg
    return render(request, 'login.html', {'error' : error, 'username' : username, 'password' : password})
