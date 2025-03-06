from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from logic.models import Account

@login_required
def index(request):
    accounts = Account.objects.filter(user=request.user)  # Получаем счета только текущего пользователя
    return render(request, "interface/index.html", {"accounts": accounts})
