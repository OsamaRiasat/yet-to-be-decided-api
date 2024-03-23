from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactSubmission(models.Model):
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
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES, default='Agriculture', verbose_name=_('industry'), blank=False)

    def __str__(self):
        return self.name


class MeetingRequest(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('created on'))

    name = models.CharField(verbose_name=_('name'), max_length=100, blank=False)
    email = models.EmailField(verbose_name=_('email'), max_length=100, blank=False)
    message = models.TextField(verbose_name=_('message'), blank=True)
    datetime = models.DateTimeField(verbose_name=_('datetime'), blank=False)

    def __str__(self):
        return self.name


class NewsletterSubscription(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('created on'))

    email = models.EmailField(verbose_name=_('email'), max_length=100, blank=False)

    def __str__(self):
        return self.email

