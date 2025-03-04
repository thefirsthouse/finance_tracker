from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models

@login_required
def create_account(request):
    if request.method == "POST":
        form = forms.CreateAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user  # Установить текущего пользователя
            account.save()
            return redirect('profile')  # Замените 'profile' на имя представления, куда нужно перенаправить после сохранения
    else:
        form = forms.CreateAccountForm()
    return render(request, "logic/create_account.html", {"form": form})

@login_required
def create_transfer(request):
    if request.method == "POST":
        form = forms.RecordForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('profile')  # Замените 'some_view_name' на имя представления, куда нужно перенаправить после сохранения
    else:
        form = forms.RecordForm()
    return render(request, 'logic/create_transfer.html', {'form': form})


@login_required
def create_record(request):
    if request.method == "POST":
        form = forms.RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)  # Получаем объект, но не сохраняем
            record.account = request.user.account  # Привязываем к аккаунту пользователя
            record.save()
    else:
        form = forms.RecordForm()
    return render(request, "logic/create_record.html", {"form": form})
