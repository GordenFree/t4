
from django.http import HttpResponse
from .models import Bboard


# Create your views here.
def index(request):
    s = 'Cписок обьявлений\r\n\r\n\r\n'
    for bb in Bboard.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
