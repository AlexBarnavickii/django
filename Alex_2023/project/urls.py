from django.contrib import admin
from django.urls import path
from . import views
app_name = 'projects'
urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("blog", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<int:pk>/comments/", views.comments, name="comments")
]
