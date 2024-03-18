from django.urls import path, include

from .views import ContactSubmissionView, MeetingRequestView, NewsletterSubscriptionView

urlpatterns = [
    # path('contact-submission-choices/<str:field_name>/', ChoicesAPIView.as_view(), name='contact-submission-choices'),
    path('contact-submissions/', ContactSubmissionView.as_view()),
    
    path('meeting-requests/', MeetingRequestView.as_view()),
    # path('meeting-request-choices/<str:field_name>/', ChoicesAPIView.as_view(), name='meeting-request-choices'),
    
    path('newsletter-subscriptions/', NewsletterSubscriptionView.as_view()),
]
