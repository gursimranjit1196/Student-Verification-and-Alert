from django.shortcuts import render,render_to_response,RequestContext
from .forms import UserRegisForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

# Create your views here.

def signup(request) :
   
    form=UserRegisForm(request.POST or None)
    if form.is_valid() :
        save_it=form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('/register/sreg')
    return render_to_response("register/signup.html",locals(),context_instance=RequestContext(request))


def sreg(request):
    return render_to_response("register/suc-reg.html")