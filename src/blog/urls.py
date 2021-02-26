from .views import (blog_post_detail_view, blog_post_list_page, 
blog_post_update_view, blog_post_delete_view)
from django.urls import path

urlpatterns = [
    path('', blog_post_list_page),
    path('<slug:slug>/', blog_post_detail_view),
    path('<slug:slug>/edit/', blog_post_update_view),
    path('<slug:slug>/delete/', blog_post_delete_view),
]
