from django.shortcuts import render
# helloworld/helloworld/view.py
from django.http import HttpResponse,Http404

def index(request):
    return HttpResponse("Hello world !  django ~~")
def demo(request):
    return render(request,'demo.html')
def home(request):
    return render(request,'home.html')
def page(request,num):
    try:
        num = int(num)
        return render(request, 'demo.html')
    except:
        raise Http404
#def home(request, year="2018", month="01"):
    #return HttpResponse("获取当前页面home时间标签：%s年/%s月" %(year, month))
def home1(request, year="2018", month="01"):
    return HttpResponse("获取当前页面home时间标签：%s年/%s月" %(year, month))
def lan(request):
    context = {}
    context['name'] = '蓝水源'
    return  render(request,'lan.html', context)
def fenceng(request):
    context = {"name": "水源"}
    return render(request, 'fenceng.html', context)
def sonblock(request):
    context = {"ads":["appnium","selenium","request"]}
    return render(request,'sonblock.html', context )






