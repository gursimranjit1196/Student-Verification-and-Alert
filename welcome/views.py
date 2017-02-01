from django.shortcuts import render

from django.shortcuts import render,render_to_response,RequestContext

from django.http import HttpResponse
from django.http import HttpResponseRedirect

def welcome(request):
    return render_to_response("welcome/welcome.html", locals(), context_instance=RequestContext(request))









# Create your views here.
