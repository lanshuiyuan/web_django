from django.shortcuts import render
# helloworld/helloworld/view.py
from django.http import HttpResponse,Http404

def index(request):
    return HttpResponse("Hello world !  django ~~")
def demo(request):
    return render(request,'demo.html')
def page(request,num):
    try:
        num = int(num)
        return render(request, 'demo.html')
    except:
        raise Http404

