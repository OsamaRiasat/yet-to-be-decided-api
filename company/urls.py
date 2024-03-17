from django.urls import path, include

from .views import ContactSubmissionView, ChoicesAPIView

urlpatterns = [
    path('contact-submission-choices/<str:field_name>/', ChoicesAPIView.as_view(), name='contact-submission-choices'),
    path('contact-submissions/', ContactSubmissionView.as_view()),
]
