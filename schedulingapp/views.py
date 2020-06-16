from datetime import datetime
from django.shortcuts import render,reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def test1(request,url):
    return HttpResponse(status=200)
    #get request on url specified returns status code 200

def test(request,url,date):
    now=datetime.now()
    s=str(now.year)+"-"+str(now.month)+'-'+str(now.day)+'-'+str(now.hour)+'-'+str(now.minute)
    if str(date)==str(s):
        return HttpResponseRedirect((reverse('test1',args=(url,))))
        #when current Date-Time matches the one specified in Date-Time parameter, get request sent to specified url parameter
    else:
        return HttpResponse(status=404)
        #if current Date-Time does not match the one specified in Date-Time parameter, status code 400 returned

def home(request):
    return HttpResponseRedirect((reverse('test',args=('tryurl','2020-6-17-1-41',))))
    #call made to API with two parameters, url and date time


def ping(request):
    return JsonResponse({"status":"OK"})
    #when GET request is sent to the '/ping' endpoint, server returns JSON "{ "status":"OK"}"

