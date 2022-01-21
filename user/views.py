from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        bio = request.POST.get('bio')        

        if password != password2:
            msg = {'msg':'패스워드를 확인해 주세요.'}
            return render(request, 'user/signup.html', msg)
        elif get_user_model().objects.filter(username=username):
            msg = {'msg':'이미 존재하는 아이디입니다.'}
            return render(request, 'user/signup.html', msg)
        elif username=='' or password=='' or password2=='':
            msg = {'msg':'정보가 누락된 곳이 있습니다.'}
            return render(request, 'user/signup.html', msg)                     
        
        UserModel.objects.create_user(username=username, password=password, bio=bio)

        return redirect('signin')  

    else:
        user = request.user.is_authenticated
        if user:
            return redirect('tweet')
        else:
            return render(request, 'user/signup.html')


def sign_in_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        login_user = auth.authenticate(request, username=username, password=password)

        if login_user:
            auth.login(request, login_user)   
            return redirect('tweet')
        else:            
            return redirect('signin')
    else:
        user = request.user.is_authenticated
        if user:
            return redirect('tweet')
        else:
            msg = {'msg':'ID 혹은 비밀번호를 확인 해 주세요.'}
            return render(request, 'user/signin.html', msg)
        

@login_required
def logout(request):
    auth.logout(request)
    return redirect('signin')


'''
User following features
'''
@login_required
def user_list(request):
    if request.method == 'GET':
        login_user = request.user
        users = get_user_model().objects.all().exclude(username=request.user.username)
        context = {'users':users, 'login_user':login_user}
        return render(request, 'user/user_list.html', context)


@login_required
def user_follow(request, id):
    selected_user = get_user_model().objects.get(id=id)
    if request.user in selected_user.followee.all():
        selected_user.followee.remove(request.user)
    else:
        selected_user.followee.add(request.user)
    return redirect('user_list')



