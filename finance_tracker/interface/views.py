from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from logic.models import Account, Record

@login_required
def index(request):
    accounts = Account.objects.filter(user=request.user)
    records = Record.objects.filter(account__in=accounts).order_by('-date_time')[:5]
    return render(request, "interface/index.html", {"accounts": accounts, "records": records})


def records_list(request):
    sort = request.GET.get('sort')

    if sort == 'date':
        records = Record.objects.order_by('-date_time')
    elif sort == 'category':
        records = Record.objects.order_by('category__name')
    elif sort == 'type':
        records = Record.objects.order_by('type_of')
    else:
        records = Record.objects.all().order_by('-date_time')
    
    return render(request, 'interface/record_list.html', {'records': records})
