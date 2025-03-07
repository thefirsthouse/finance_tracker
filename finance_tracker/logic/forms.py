from django import forms

from . import models


class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ['name', 'currency']
        labels = {
            'name': 'Account name',
            'currency': 'Account currency',
        }


class RecordForm(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = ['type_of', 'account', 'category', 'amount', 'date_time']
        labels = {
            'type_of': 'Type',
            'category': 'Category',
            'amount': 'Amount',
            'date_time': 'Date and time',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['account'].queryset = models.Account.objects.filter(user=user)
