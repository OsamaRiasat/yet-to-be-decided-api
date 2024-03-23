from django.shortcuts import render
from .models import ContactSubmission, MeetingRequest, NewsletterSubscription
from .serializers import ContactSubmissionSerializer, MeetingRequestSerializer, NewsletterSubscriptionSerializer


from rest_framework.response import Response
from rest_framework import status, generics

from rest_framework.views import APIView

# Create your views here.

class ContactSubmissionView(generics.ListCreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

    def post(self, request, *args, **kwargs):
        serializer = ContactSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data': serializer.data,
                'message': 'Your message has been sent. We will get back to you soon.'
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'data': serializer.errors,
            'message': 'Could not send your message. Please try again.'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MeetingRequestView(generics.ListCreateAPIView):
    queryset = MeetingRequest.objects.all()
    serializer_class = MeetingRequestSerializer

    def post(self, request, *args, **kwargs):
        """
        - Datetime format: YYYY-MM-DDTHH:MM:SS.sssZ
        """
        serializer = MeetingRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data': serializer.data,
                'message': 'Your meeting request has been sent. We will get back to you soon.'
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'data': serializer.errors,
            'message': 'Could not send your meeting request. Please try again.'
        }
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsletterSubscriptionView(generics.ListCreateAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer

    def post(self, request, *args, **kwargs):
        serializer = NewsletterSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                'data': serializer.data,
                'message': 'You have been successfully subscribed to our newsletter.'
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'data': serializer.errors,
            'message': 'Could not subscribe you to our newsletter. Please try again.'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

