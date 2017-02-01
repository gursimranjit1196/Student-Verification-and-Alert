from django.shortcuts import render
from django.core.context_processors import csrf

from django.shortcuts import render,render_to_response,RequestContext

from django.http import HttpResponse
from django.http import HttpResponseRedirect

def createqr(request):
    return render_to_response("adminn/createqr.html", locals(), context_instance=RequestContext(request))

def adminpage(request):
    return render_to_response("adminn/adminpage.html", locals(), context_instance=RequestContext(request))

def scanqr(request):
    return render_to_response("adminn/scanqr.html", locals(), context_instance=RequestContext(request))

def checkadmin(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('adminn/checkadmin.html', c)

def check(request):
    print('check me h')
    username3 = request.POST.get('username')
    password3 = request.POST.get('password')
    print(username3)
    print(password3)
    if username3=='gursi' and password3=='gursi':
        return HttpResponseRedirect('/adminn/adminpage/')
    else:
        return HttpResponseRedirect('/adminn/checkadmin/')

    #return render_to_response('signin/invalid.html')







# Create your views here.
