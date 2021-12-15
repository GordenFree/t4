
from django.shortcuts import render

from .models import Bboard, Rubric


# Create your views here.
def index(request):
    bbs = Bboard.objects.all()
    context = {'bbs':bbs}
    return render(request, 'main/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bboard.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(request, 'main/by_rubric.html', context)