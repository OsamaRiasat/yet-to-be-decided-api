from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactSubmission(models.Model):
    REGION_CHOICES = (
        ('Middle East and North Africa', 'Middle East and North Africa'),
        ('USA', 'USA'),
        ('Europe', 'Europe'),
        ('Asia', 'Asia'),
        ('Australia', 'Australia'),
        ('Africa', 'Africa'),
        ('South America', 'South America'),
        ('Central America', 'Central America'),
        ('Caribbean', 'Caribbean'),
        ('Other', 'Other'),
    )

    INDUSTRY_CHOICES = (
        ('Agriculture', 'Agriculture'),
        ('Automotive', 'Automotive'),
        ('Banking', 'Banking'),
        ('Construction', 'Construction'),
        ('Education', 'Education'),
        ('Energy', 'Energy'),
        ('Entertainment', 'Entertainment'),
        ('Fashion', 'Fashion'),
        ('Finance', 'Finance'),
        ('Food and Beverage', 'Food and Beverage'),
        ('Healthcare', 'Healthcare'),
        ('Hospitality', 'Hospitality'),
        ('Insurance', 'Insurance'),
        ('Manufacturing', 'Manufacturing'),
        ('Media', 'Media'),
        ('Pharmaceutical', 'Pharmaceutical'),
        ('Real Estate', 'Real Estate'),
        ('Retail', 'Retail'),
        ('Technology', 'Technology'),
        ('Telecommunications', 'Telecommunications'),
        ('Transportation', 'Transportation'),
        ('Travel', 'Travel'),
        ('Utilities', 'Utilities'),
        ('Other', 'Other'),
    )

    created_on = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('created on'))

    name = models.CharField(verbose_name=_('name'), max_length=100, blank=False)
    email = models.EmailField(verbose_name=_('email'), max_length=100, blank=False)
    message = models.TextField(verbose_name=_('message'), blank=False)
    region = models.CharField(max_length=100, choices=REGION_CHOICES, default='Middle East and North Africa')
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES, default='Agriculture', verbose_name=_('industry'), blank=False)

    def __str__(self):
        return self.name
