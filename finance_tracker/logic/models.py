from django.db import models
from django.conf import settings

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
    name = models.CharField(verbose_name='Name', max_length=20, unique=True, blank=True)
    currency = models.CharField(verbose_name='Currency', choices=CURRENCIES, default=CURRENCIES[3], max_length=30)

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


class Transfer(models.Model):
    TYPES = [
        ('income', 'Income'),
        ('expence', 'Expence'),
        ('transfer', 'Transfer')
    ]
    type_of = models.CharField(verbose_name='Type', max_length=15, default='expence', choices=TYPES)
    account = models.ForeignKey(Account, models.CASCADE, related_name='transfers')
    category = models.ForeignKey(Category, models.CASCADE, related_name='transfers')
    amount = models.FloatField(verbose_name='Amount', blank=True, editable=True)
    date_time = models.DateTimeField(verbose_name='Date and time', editable=True)  # Сделать поле редактируемым