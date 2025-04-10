from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from .forms import RecordForm

@login_required
def create_account(request):
    if request.method == "POST":
        form = forms.CreateAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('main')
    else:
        form = forms.CreateAccountForm()
    return render(request, "logic/create_account.html", {"form": form})

@login_required
def create_transfer(request):
    if request.method == "POST":
        form = forms.RecordForm(request.POST, user=request.user)
        if form.is_valid():
            record = form.save(commit=False)
            account = record.account
            account.balance -= record.amount
            account.save()
            record.save()
            return redirect('main')
    else:
        form = RecordForm(user=request.user)
    return render(request, 'logic/create_transfer.html', {'form': form})


@login_required
def create_record(request):
    if request.method == "POST":
        form = forms.RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.account = request.user.account
            record.save()
    else:
        form = forms.RecordForm()
    return render(request, "logic/create_record.html", {"form": form})
