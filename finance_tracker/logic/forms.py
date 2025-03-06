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
