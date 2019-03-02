from django.shortcuts import render, redirect, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Article, User, Comment
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'jianshu/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        return Article.objects.order_by('article_created_time')

def article_content(request, article_id):
    templates = loader.get_template('jianshu/article_content.html')
    article = Article.objects.filter(article_id=article_id).first()
    article = {
        'article_title': article.article_title,
        'article_context': article.article_context,
    }
    return HttpResponse(templates.render(article, request))

@csrf_exempt
def write_article(request):
    info = {
        'created_time': timezone.now(),
    }
    if request.method == 'GET':
        templates = loader.get_template('jianshu/write.html')
        return HttpResponse(templates.render(info, request))
    else:
        article_title = request.POST['title']
        article_context = request.POST['context']
        article = Article.objects.filter(article_title=article_title).first()
        if article:
            return 'article exist'
        else:
            Article.objects.create(article_title=article_title,
                                   article_context=article_context,
                                   article_created_time=info['created_time'])
            return redirect('index')

@csrf_exempt
def write_comment(request, article_id):
    article = Article.objects.filter(article_id=article_id).first()
    info = {
        'title' : article.article_title,
        'context' : article.article_context,
        'created_time' : article.article_created_time,
        'comment_created_time': timezone.now(),
    }
    if request.method == 'GET':
        templates = loader.get_template('jianshu/write_comment.html')
        return HttpResponse(templates.render(info, request))
    else:
        comment_context = request.POST['comment']
        Comment.objects.create(article_id=article_id,
                               comment_context=comment_context,
                               comment_create_time=info['comment_created_time'])
        return redirect('index')

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'jianshu/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(user_name=username, user_password=password).first()
        if user:
            login_user = User.objects.get(user_name=username, user_password=password)
            print(user.user_name, login_user)
            response = redirect("index")
            response.set_cookie("user_name", user.user_name, 604800)
            return response
        else:
            return 'error password or username'

def logout(request):
    response = redirect("login")
    response.delete_cookie("user_name")
    return response

@csrf_exempt
def register(request):
    print(register)
    if request.method == 'GET':
        return render(request, 'jianshu/register.html')
    else:
        username = request.POST['username']
        telephone = request.POST['telephone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user_tel = User.objects.filter(user_tel=telephone).first()
        user_name = User.objects.filter(user_name=username).first()
        if user_tel == None and user_name == None:
            if password1 != password2:
                return 'please enter your password again.'
            else:
                User.objects.create(user_name=username,
                                user_tel=telephone,
                                user_password=password2)
                return redirect("login")
        else:
            return 'tel exist.'
