from django.shortcuts import render
from .models import Project
from .models import Comment
from django.http import HttpResponse
from django.urls import reverse
def project_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    a = Project.objects.get(id=pk)
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    comments_list = a.comment_set.order_by('-id')
    return render(request, 'project_detail.html',  {'comments_list' : comments_list})


#####################################################
def blog_index(request):
    projects = Comment.objects.order_by('-cteated_on')
    context = {
        'projects': projects
    }
    return render(request, 'blog_index.html', {'projects': projects})

def blog_detail(request, pk):
    project = Comment.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'blog_detail.html', context)

def comments(request, project_id):
    a = Project.objects.get(id = project_id)
    a.comments_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponse('project:project_detail', args = (a.id,))