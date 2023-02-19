from django.shortcuts import render
from .models import Project
from .models import Comment


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


#####################################################
def blog_index(request):
    projects = Comment.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'blog_index.html', context)

def blog_detail(request, pk):
    project = Comment.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'blog_detail.html', context)


