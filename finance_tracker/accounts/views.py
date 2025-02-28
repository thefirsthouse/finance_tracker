from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# from .forms import LoginUserForm


# def login_user(request):
#     if request.method == "POST":
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], email=
#                 cd['email'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#             return HttpResponseRedirect(reverse('home'))
#     return render(request, 'accounts/login', context={'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
