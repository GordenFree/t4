
from django.shortcuts import render

from django.urls import reverse_lazy

from .models import Bboard, Rubric

from django.views.generic.edit import CreateView

from .forms import BboardForm

class BboardCreateView(CreateView):
    template_name = 'main/create.html'
    form_class = BboardForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

# Create your views here.
def index(request):
    bbs = Bboard.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics':rubrics}
    return render(request, 'main/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bboard.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(request, 'main/by_rubric.html', context)

def about(request):
    return render (request, 'main/about.html')