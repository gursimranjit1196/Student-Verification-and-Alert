from django.shortcuts import render

from django.shortcuts import render,render_to_response, RequestContext

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Timetable

# Create your views here.


def detail(request):
    dispdet=Timetable.objects.all()
    context={'dispdet':dispdet}
    return render(request,"schedule/det.html",context)
