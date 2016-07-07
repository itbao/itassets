from django.shortcuts import render

from django.shortcuts import render_to_response
# Create your views here.

def table(request):
    return render_to_response('table.html')



# ---------------------------------------------------------------
from itassets.models import *

def info(request):
    cpulist= cpus.objects.all()
    return render_to_response('server_manager.html',{'user':request.user,'iplist' : iplist})






#----------------------------------------------------------------
from django.http import HttpResponse

import datetime


    





def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
            message='You searchd for : %r' % request.GET['q']
    else:
            message='You submitted an empty form.'
    return HttpResponse(message)


def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


from django.http import Http404, HttpResponse

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
