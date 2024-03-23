from django.urls import path, include

from .views import ContactSubmissionView, MeetingRequestView, NewsletterSubscriptionView

urlpatterns = [
    path('contact-submissions/', ContactSubmissionView.as_view()),
    path('meeting-requests/', MeetingRequestView.as_view()),    
    path('newsletter-subscriptions/', NewsletterSubscriptionView.as_view()),
]
