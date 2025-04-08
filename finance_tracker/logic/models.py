from django.db import models
from django.conf import settings
from django.utils import timezone

class Account(models.Model):
    CURRENCIES = [
        ('usd', 'US Dollar'),
        ('eur', 'EU Euro'),
        ('cny', 'CN Yuan'),
        ('rub', 'RU Rouble'),
        ('aed', 'AE Dirham'),
        ('azn', 'AZ Manat'),
        ('btc', 'Bitcoin'),
        ('byn', 'BY Rouble'),
        ('gel', 'GR Lari'),
        ('ils', 'IS Sheqel'),
        ('ind', 'IN Rupee'),
        ('kgs', 'KG Som'),
        ('kpw', 'NK Won'),
        ('kzt', 'KZ Tenge'),
        ('ngn', 'NG Laira'),
        ('rsd', 'RS Dinar'),
        ('sar', 'SA Riyal'),
        ('tjs', 'TJ Somoni'),
        ('tmt', 'TM Manat'),
        ('try', 'TR Lira'),
        ('uzs', 'UZ Com'),
        ('zar', 'SA Rand')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='accounts')
    name = models.CharField(verbose_name='Name', max_length=20, blank=True)
    currency = models.CharField(verbose_name='Currency', choices=CURRENCIES, default=CURRENCIES[3], max_length=30)
    balance = models.FloatField(verbose_name='Balance', default=0)

    def __str__(self):
        return self.name


class Category(models.Model):
    NATURES = [
        ('none', 'None'),
        ('must', 'Must'),
        ('need', 'Need'),
        ('want', 'Want'),
    ]
    name = models.CharField(verbose_name='Group', max_length=30)
    nature = models.CharField(verbose_name='Nature', max_length=5, choices=NATURES, default=NATURES[0])
    spent = models.FloatField(verbose_name='Spent', default=0)

    def __str__(self):
        return self.name


class Record(models.Model):
    TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
        ('transfer', 'Transfer')
    ]
    type_of = models.CharField(verbose_name='Type', max_length=15, default='expense', choices=TYPES)
    account = models.ForeignKey(Account, models.CASCADE, related_name='records')
    category = models.ForeignKey(Category, models.CASCADE, related_name='records')
    amount = models.FloatField(verbose_name='Amount')
    date_time = models.DateTimeField(verbose_name='Date and time', default=timezone.now)


    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.type_of == "income":
                self.account.balance += self.amount
            elif self.type_of == "expense":
                self.account.balance -= self.amount
        else:
            # if record is updates, amount delta must affect on balance
            old_record = Record.objects.get(pk=self.pk)
            if old_record.type_of == "income":
                self.account.balance -= old_record.account
            elif old_record.type_of == "expense":
                self.account.balance += old_record.amount
            
            if self.type_of == 'income':
                self.account.balance += self.amount
            elif self.type_of == 'expense':
                self.account.balance -= self.amount
        
        self.account.save()
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.get_type_of_display()} - {self.amount} ({self.date_time.strftime('%Y-%m-%d %H:%M')})"



class Transfer(models.Model):
    account1 = models.ForeignKey(Account, models.CASCADE, related_name='transfer_from')
    account2 = models.ForeignKey(Account, models.CASCADE, related_name='transfer_to')
    amount = models.FloatField(verbose_name='Amount', blank=True, editable=True)
    date_time = models.DateTimeField(verbose_name='Date and time', editable=True)
