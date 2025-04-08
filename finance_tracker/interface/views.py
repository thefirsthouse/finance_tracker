from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from logic.models import Account, Record

@login_required
def index(request):
    accounts = Account.objects.filter(user=request.user)
    records = Record.objects.all().order_by('-date_time')[:5]
    return render(request, "interface/index.html", {"accounts": accounts, "records": records})
