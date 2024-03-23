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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MeetingRequestView(generics.ListCreateAPIView):
    queryset = MeetingRequest.objects.all()
    serializer_class = MeetingRequestSerializer

    def post(self, request, *args, **kwargs):
        """
        - Date format: YYYY-MM-DD
        - Time format: HH:MM:SS
        """
        serializer = MeetingRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsletterSubscriptionView(generics.ListCreateAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer

    def post(self, request, *args, **kwargs):
        serializer = NewsletterSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

