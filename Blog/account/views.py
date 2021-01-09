from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def sign_in(request):
    data = {}
    if request.method == "GET":
        if request.user.is_authenticated:
            data['report'] = 'User is already authenticated'
            print(data['report'])
            return render(request, 'account/result.html', context=data)
        return render(request, 'account/login.html')

    elif request.method == "POST":
        _login = request.POST.get('login_field')
        _password = request.POST.get('password_field')
        user = authenticate(request, username=_login, password=_password)

        if user is None:
            data['report'] = 'User not found or wrong password'
            print(data['report'])
            return render(request, 'account/result.html', context=data)
        else:
            data['report'] = 'You have successfully authenticated'
            print(data['report'])
            login(request, user)
            return render(request, 'account/result.html', context=data)


def logout_user(request):
    logout(request)
    return redirect('/')


def register(request):
    data = dict()
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'account/register.html', context={})

    elif request.method == "POST":
        print('post')
        login = request.POST.get('login_field')
        email = request.POST.get('email_field')
        passwd1 = request.POST.get('password_field')
        passwd2 = request.POST.get('password_confirmation_field')

        data['login'] = login
        data['email'] = email
        data['passwd1'] = passwd1
        data['passwd2'] = passwd2

        if passwd1 != passwd2:
            report = 'Passwords must match'
            print(data['report'])
        elif '' in data.values():
            report = 'All fields are required'
            print(data['report'])
        elif len(passwd1) < 8:
            report = 'The password is too short'
            print(data['report'])
        else:
            user = User.objects.create_user(login, email, passwd1)
            user.save()
            if user:
                data['report'] = 'You have successfully registered'
                print(data['report'])
                return render(request, 'account/result.html', context=data)
            report = 'Oops! Something wrong.'
        data['report'] = report
        print(data['report'])
        return render(request, 'account/result.html', context=data)


def result(request):
    return render(request, 'account/result.html')


def ajax_reg(request) -> JsonResponse:
    response = dict()
    _login = request.GET.get('login_field')
    try:
        User.objects.get(username=_login)
        response['message_login'] = 'занят'
    except User.DoesNotExist:
        response['message_login'] = 'свободен'

    return JsonResponse(response)


def ajax_log_passwd(request) -> JsonResponse:
    response = dict()

    _login = request.GET.get('login_field')
    _password = request.GET.get('password_field')

    user = authenticate(request, username=_login, password=_password)
    if user is not None:
        response['message_user'] = 'ok'
        # login(request, user)
        return JsonResponse(response)
    else:

        response['message_user'] = 'error'
        return JsonResponse(response)
