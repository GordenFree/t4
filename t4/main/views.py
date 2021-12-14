
from django.http import HttpResponse
from django.template import loader

from .models import Bboard


# Create your views here.
def index(request):
    template = loader.get_template('main/index.html')
    bbs = Bboard.objects.order_by('-published')
    context = {'bbs':bbs}
    return HttpResponse(template.render(context, request))
