from django.contrib import admin
from .models import ContactSubmission, MeetingRequest, NewsletterSubscription

# Register your models here.

admin.site.register(ContactSubmission)
admin.site.register(MeetingRequest)
admin.site.register(NewsletterSubscription)