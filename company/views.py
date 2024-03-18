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

    def get_region_choices(self):
        return ContactSubmission.REGION_CHOICES

class ChoicesAPIView(APIView):
    def get(self, request, field_name):
        """
        Get choices for a field.
        Parameters:
        - REGION
        - INDUSTRY
        """
        try:
            choices = dict(getattr(ContactSubmission, f'{field_name.upper()}_CHOICES'))
            return Response(choices)
        except AttributeError:
            return Response({'error': f'Field "{field_name}" does not exist or does not have choices.'}, status=400)


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

    def get_region_choices(self):
        return MeetingRequest.REGION_CHOICES


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

