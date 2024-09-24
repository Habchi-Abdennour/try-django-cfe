from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ArticlesForms
# Create your views here.
@login_required
def index(request):
    context=Articles.objects.all()
    return render(request,'templates/index.html',{'data':context})


def article_Detail(request,article_id):
    context=Articles.objects.get(id=article_id)
    return render(request,'templates/article_Detail.html',{'data':context})

def search(request):
    query_search=request.GET
    query=query_search.get('q')
    if query is not None:
        context=Articles.objects.get(id=query)
        return render(request,'search.html',{'search':context})
    else:
        return render(request,'search.html')
    
@login_required
def create_article(request):
    form=ArticlesForms(request.POST or None)
    context={
        'forms':form,  }
    if request.method=='POST':
        if form.is_valid():
            Arcticle_object=form.save()
            context['forms']=ArticlesForms()
            context['object']=Arcticle_object
            context['created']=True
        
    
    return render(request,'templates/create.html',context)


def update():
    pass
    return