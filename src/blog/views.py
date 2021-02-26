from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.



def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    #queryset = BlogPost.objects.filter(slug=slug)
    #if queryset.count() != 1:
    #    raise Http404
    #if queryset.count() >= 1:
    #    obj = queryset.first()
    template_name = 'blog_post_detail.html'
    context = {'object':obj}
    return render(request, template_name, context)


def blog_post_list_page(request):
    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {'object_list':qs}
    return render(request, template_name, context)

@login_required()
def blog_post_create_view(request):
    if not request.user.is_authenticated:
        return render(request, 'not-a-user.html')
    template_name = 'blog/form.html'
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        #BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostForm()
    context = {'form':form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    template_name = 'blog/detail.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {'object':obj}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    template_name = 'blog/update.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {'object':obj, 'form':None}
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    template_name = 'blog/delete.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {'object':obj}
    return render(request, template_name, context)