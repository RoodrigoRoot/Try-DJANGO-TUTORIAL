from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
    context = {'title':'Home Page'}
    qs = BlogPost.objects.all()[:5]
    context = {'title':'Welcomw to Try Django', 'blog_list':qs}
    #template_name = 'title.txt'
    #template_obj = get_template(template_name)
    #rendered_string = template_obj.render(context)
    #print(rendered_string)
    return render(request, 'home.html', context)

def about_page(request):
    my_title = 'About Us'
    return render(request, 'about.html', locals())

def contact_page(request):
    my_title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    return render(request, 'form.html', locals())


def example_page(request):
    context = {'my_title':'Examples page'}
    template_name = 'hello_world.html'
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)