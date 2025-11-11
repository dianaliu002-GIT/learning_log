from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse  
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # 获取表单提交的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 验证用户
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # 验证成功：注册登录状态
            login(request, user)
            # 强制跳转到 topics 页面（无视 next 参数，确保跳转）
            return redirect('learning_logs:topics')
        else:
            # 验证失败：返回登录页并提示错误
            messages.error(request, '用户名或密码错误，请重新输入')
            return render(request, 'users/login.html')
    else:
        # GET 请求：显示登录表单
        return render(request, 'users/login.html')

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            print("开始保存用户...")  # 新增打印
            new_user = form.save()
            print("用户保存成功！")  # 新增打印
            # 让用户自动登录，再重定向到主页
            authenticate_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)