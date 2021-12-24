from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView ,DetailView,CreateView,DeleteView,UpdateView
from .models import BlogModel
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
def welcome_html_temprate(request):
    return render(request,'welcome.html')


class BlogList(ListView):
    template_name ='list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name ='detail.html'
    model = BlogModel

class BlogCreate(CreateView):
    template_name='create.html'
    model= BlogModel
    fields ={'title','content','category'}
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    template_name='delete.html'
    model= BlogModel
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    template_name='update.html'
    model= BlogModel
    fields =('title','content','category')
    success_url = reverse_lazy('list')

def signupview(request):
    if request.method =='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        try:
            User.objects.create_user(username_data,'',password_data)
        except IntegrityError:
            return render(request,'signup.html',{'error':' このユーザーは既に登録されています。'})
    else:
        return render(request,'signup.html',{})
    return render(request,'signup.html',{})

def loginview(request):
    if request.method=='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request,'login.html')