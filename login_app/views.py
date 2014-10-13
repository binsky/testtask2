from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    return render(request, 'login.html')


def auth_and_login(request):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        # return render(request, 'sort.html')
        return redirect('/sort')
    else:
        return render(request, 'login.html', {'error': 'Unknown account. Try again.'})



