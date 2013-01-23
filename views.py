from django.shortcuts import render_to_response, get_object_or_404
from models import Project
from helpers import collect_updates
from django.http import HttpResponse

def main(request):
    return render_to_response("frontpage/frontpage.html", {
    })

def project(request, slug):
    project = get_object_or_404(Project, slug=slug)

    return render_to_response("frontpage/project.html", {
        'project': project,
    })

def project_list(request):
    return render_to_response("frontpage/project_list.html", {
        'projects': Project.objects.all().order_by("-updated"),
    })

def update_feed(request):
    page = request.GET.get('page', '1');
    project = request.GET.get('project');
    response = collect_updates(page, project)
    return HttpResponse(response, content_type='application/json')
