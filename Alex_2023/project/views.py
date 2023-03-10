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
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


#####################################################
def blog_index(request):
    comments = Comment.objects.order_by('-cteated_on')
    context = {'comments': comments}
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    comment = Comment.objects.get(pk=pk)
    context = {'comment': comment}
    return render(request, 'blog_detail.html', context)


# def comments(request, project_id):
#     a = Project.objects.get(id=project_id)
#     a.comments_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
#     return HttpResponse('project_detail', args=(a.id,))
#
#
# def azs(request, id):
#     project = Comment.objects.objects.get(id=id)
#     context = {'project': project}
#     return render(request, 'blog_detail.html', context)
