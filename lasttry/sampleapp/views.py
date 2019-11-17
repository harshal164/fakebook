from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import user, fileModel, comments
import re
from .forms import RegisterForm,registerForm2,loginForm,fileForm, commentForm
from  django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def getuser_details(request, tname):
    obj = get_object_or_404(user,username=tname)
    """try:
        obj = user.objects.get(name=tname)
    except user.DoesNotExist:
        raise Http404"""
    tmpname = 'user_details_template.html'
    context = {"object":obj}
    return render(request,tmpname,context)
#GET -> 1 object
#FILTER -> multiple objects
def dashboard(request):
    if(request.session.get('user',None) == None):
        return redirect('/login/')
    x = request.GET.get('f' or None)
    if x == None:
        x = int(0)
    else:
        x = int(x)
    q_set = fileModel.objects.all().order_by('-timestamp')[x:x+10]
    form = fileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(request.FILES)
        obj = form.save(commit=False)
        obj.username = request.session.get('user',None)
        obj.save()
        form = fileForm()
    t = "dashboard2.html"
    c = {"q":q_set,"username":request.session['user'],"form":form,"x":x}
    return render(request,t,c)

def showpost(request):
    if (request.session.get('user', None) == None):
        return redirect('/login/')
    id = request.GET.get('id' or None)
    form = commentForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.username = request.session.get('user', None)
        obj.postid = request.GET.get('id')
        obj.save()
        form = commentForm()
    try:
        cm = comments.objects.filter(postid=id)
    except comments.DoesNotExist:
        cm = None
    c = {'id':id,'fm':fileModel.objects.get(id=id),'c':cm,'form':form}
    t = 'showpost.html'
    return render(request,t,c)


def user_create(request):
    template = 'registration_template.html'
    # form = RegisterForm(request.POST or None)
    form = registerForm2(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/')
        # obj = user.objects.create(**form.cleaned_data)
        form = registerForm2()
    context = {'form': form}
    return render(request, template, context)

def logout(request):
    del request.session['user']
    return redirect('/login/')

def user_update(request):
    if (request.session.get('user', None) == None):
        return redirect('/login/')
    obj = get_object_or_404(user, username=request.session.get('user'))
    form = registerForm2(request.POST or None, request.FILES or None, instance = obj)
    tmpname = 'user_update.html'
    # print(obj.__dict__)
    context = {"form":form}
    response = HttpResponse(render(request, tmpname, context))
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        response = redirect('/getuser_details/{}/'.format(obj.__dict__['username']))
    return response


def login(request):
    request.session['user'] = None
    form = loginForm(request.POST or None)
    tmpname = 'login_template.html'
    context = {'form':form}
    response = HttpResponse(render(request, tmpname, context))
    if form.is_valid():
        try:
            obj = user.objects.get(username=form.cleaned_data['username'],pwd=form.cleaned_data['pwd'])
            request.session['user'] = obj.__dict__['username']
            print(request.session['user'])
            response = redirect('/dashboard')
        except:
            response = redirect('/')
    return response

def chatroom(request):
    if (request.session.get('user', None) == None):
        return redirect('/login/')
    t = "ws.htm"
    c = {'username':request.session.get('user')}
    return render(request,t,c)

def user_search(request):
    if (request.session.get('user', None) == None):
        return redirect('/login/')
    name = request.GET.get('q')
    q_set = user.objects.filter(name__contains=name)
    print(q_set)
    t = "dashboard_template.html"
    print(q_set.__dict__)
    c = {"q":q_set,"username":request.session['user']}
    return render(request,t,c)

def file_search(request):
    if (request.session.get('user', None) == None):
        return redirect('/login/')
    name = request.GET.get('q')
    q_set = fileModel.objects.filter(title__contains=name)
    t = "filesearch.html"
    print(q_set.__dict__)
    c = {"q":q_set,"username":request.session['user']}
    return render(request,t,c)