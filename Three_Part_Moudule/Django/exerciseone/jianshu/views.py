from django.shortcuts import render, redirect, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Article, User, Comment, Album
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone
from exerciseone import settings
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'jianshu/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        return Article.objects.order_by('article_created_time')

def article_content(request, article_id):
    templates = loader.get_template('jianshu/article_content.html')
    article = Article.objects.filter(article_id=article_id).first()
    album = Album.objects.filter(album_article=article).first()
    article = {
        'article_id': article.article_id,
        'article_title': article.article_title,
        'article_context': article.article_context,
        'album_img': album.album_img,
        'user_name': album.album_user.user_name,
    }
    return HttpResponse(templates.render(article, request))

@csrf_exempt
def write_article(request):
    user_name = request.COOKIES.get('user_name')
    if user_name == None:
        return redirect('login')
    info = {
        'user_name': user_name,
        'created_time': timezone.now(),
    }
    if request.method == 'GET':
        templates = loader.get_template('jianshu/write.html')
        return HttpResponse(templates.render(info, request))
    else:
        img = request.FILES.get('img')
        print(img)
        if not img:
            return HttpResponse('image load error!')

        user = User.objects.filter(user_name=user_name).first()
        article_title = request.POST['title']
        article_context = request.POST['context']
        if Article.objects.filter(article_title=article_title).filter():
            return HttpResponse('article exist!')
        else:
            Article.objects.create(article_title=article_title,
                                   article_context=article_context,
                                   article_created_time=info['created_time'])
            article = Article.objects.filter(article_title=article_title).first()
            image = Album(
                album_user=user,
                album_article=article,
                album_img=img,
            )
            image.save()
            return redirect('index')

@csrf_exempt
def write_comment(request, article_id):
    user_name = request.COOKIES.get('user_name')
    if user_name == None:
        return redirect('login')
    article = Article.objects.filter(article_id=article_id).first()
    info = {
        'article_id': article_id,
        'user_name': user_name,
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
            response = redirect("index")
            response.set_cookie("user_name", user.user_name, 604800)
            return response
        else:
            return render(request, 'jianshu/login.html', {'error' : 'username or password error!'})

def logout(request):
    response = redirect('login')
    response.delete_cookie("user_name")
    return response

@csrf_exempt
def register(request):
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
                return HttpResponse('please enter your password again.')
            else:
                User.objects.create(user_name=username,
                                user_tel=telephone,
                                user_password=password2)
                return redirect("login")
        else:
            return render(request, 'jianshu/register.html', {'error': 'register again!'})

