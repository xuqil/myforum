from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth

from .forms import LoginForm, RegisterForm, ModifyInfoForm, UserImgUploadForm, UserNameUpdateForm, UserPasswordUpdateForm
from .models import UserProfile


class LoginView(ListView):
    """
    用户登录
    """
    template_name = 'users/login.html'

    def get(self, request, *args):
        return render(request, self.template_name, {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            pass_word = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password = pass_word)
            if user is not None:
                login(request, user)
                return redirect(to='forum:index')
            else:
                return render(request, self.template_name, {
                    'login_form': login_form,
                    'msg': '用户信息或密码错误！'
                })
        else:
            return render(request, self.template_name, {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect(to='forum:index')


class RegisterView(ListView):
    """
    用户注册
    """
    template_name = 'users/register.html'

    def get(self, request, *args):
        register_form = RegisterForm()
        return render(request, self.template_name, {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = register_form.cleaned_data['username']
            if UserProfile.objects.filter(username=user_name):
                return render(request, self.template_name, {
                    'register_form': register_form,
                    'msg': '用户已存在'
                })
            user_email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            two_password = register_form.cleaned_data.get('two_password')
            if password != two_password:
                return render(request, self.template_name, {'register_form': register_form})
            else:
                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.email = user_email
                user_profile.password = make_password(password)
                user_profile.save()
                return render(request, 'users/login.html')
        else:
            return render(request, self.template_name, {'register_form': register_form})


def user_center(request):
    """
     用户中心
    """
    return render(request, 'users/user-center.html')


class ModifyInfoView(ListView):
    """
    修改用户信息
    """
    def post(self, request):
        user_info = ModifyInfoForm(request.POST)
        if user_info.is_valid():
            request.user.nick_name = user_info.cleaned_data['nick_name']
            request.user.email = user_info.cleaned_data['email']
            request.user.mobile = user_info.cleaned_data['mobile']
            request.user.save()
            return redirect(to='users:user_center')
        else:
            return redirect(to='users:user_center')


class UserImgUploadView(LoginRequiredMixin, View):
    """
    修改用户头像
    """
    def post(self, request):
        user_avatar = UserImgUploadForm(request.POST, request.FILES)
        if user_avatar.is_valid():
            avatar = user_avatar.cleaned_data['avatar']
            request.user.avatar = avatar
            request.user.save()
            return redirect(to='users:user_center')
        else:
            return HttpResponse("错误！请返回")


class UserNameUpdateView(LoginRequiredMixin, View):
    """
    修改用户名
    """
    def get(self, request):
        name_update_form = RegisterForm()
        return render(request, 'users/user-center.html', {'name_update_form': name_update_form})

    def post(self, request):
        name_update_form = UserNameUpdateForm(request.POST)
        if name_update_form.is_valid():
            user_name = name_update_form.cleaned_data['username']
            if UserProfile.objects.filter(username=user_name):
                return render(request, 'users/user-center.html', {'name_update_form': name_update_form, 'msg': '用户名已存在'})
            request.user.username = user_name
            request.user.save()
            return redirect(to='users:user_center')
        else:
            return render(request, 'users/user-center.html', {'name_update_form': name_update_form})


class UserPasswordUpdateView(LoginRequiredMixin, View):
    """
    修改用户密码
    """
    def get(self, request, ):
        password_update_form = UserPasswordUpdateForm()
        return render(request, 'users/user-center.html', {'password_update_form': password_update_form})

    def post(self, request):
        password_update_form = UserPasswordUpdateForm(request.POST)
        if password_update_form.is_valid():
            old_password = password_update_form.cleaned_data.get('old_password')
            new_password = password_update_form.cleaned_data.get('new_password')
            two_new_password = password_update_form.cleaned_data.get('two_new_password')
            user = auth.authenticate(username=request.user, password=old_password)
            if user is not None and user.is_active:
                if new_password != two_new_password:
                    return render(request, 'users/user-center.html', {'password_update_form_msg': "两次输入的新密码不一样"})
                else:
                    request.user.password = make_password(new_password)
                    request.user.save()
                    return render(request, 'users/login.html')
            else:
                return render(request, 'users/user-center.html', {'password_update_form': password_update_form})
        else:
            return render(request, 'users/user-center.html', {'password_update_form': password_update_form})
