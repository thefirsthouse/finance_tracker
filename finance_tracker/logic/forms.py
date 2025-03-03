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


class TransferForm(forms.ModelForm):
    class Meta:
        model = models.Transfer
        fields = ['type_of', 'category', 'amount', 'date_time']
        labels = {
            'type_of': 'Record type',
            'category': 'Category',
            'amount': 'Amount',
            'date_time': 'When'
        }
