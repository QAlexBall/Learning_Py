from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.views import generic
from .models import Article, User

class IndexView(generic.ListView):
    template_name = 'jianshu/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        return Article.objects.order_by('article_created_time')[:5]
        # return Article.objects.filter(
        #     article_created_time=timezone.now()
        # ).order_by('-article_created_time')[:5]

def write_article(request):
    return render(request, 'jianshu/write.html')

def login(request):
    return render(request, 'jianshu/login.html')

@csrf_exempt
def register(request):
    print(register)
    if request.method == 'GET':
        print('get')
        return render(request, 'jianshu/register.html')
    else:
        print(request.method)
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
                print('password is OK!')
                User.objects.create(user_name=username,
                                user_tel=telephone,
                                user_password=password2)
                return redirect('jianshu/login.html')
        else:
            return 'tel exist.'
