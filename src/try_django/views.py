from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm

def home_page(request):
    context = {'title':'Home Page'}
    if request.user.is_authenticated:
        context = {'title':'Home Page', 'my_list':[1,2,3,4,5]}
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