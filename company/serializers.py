from rest_framework import serializers
from .models import ContactSubmission, MeetingRequest, NewsletterSubscription



class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'

    def create(self, validated_data):
        return ContactSubmission.objects.create(**validated_data)

    def get_region_choices(self):
        return dict(ContactSubmission.REGION_CHOICES)


class MeetingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRequest
        fields = '__all__'

    def create(self, validated_data):
        return MeetingRequest.objects.create(**validated_data)

    def get_region_choices(self):
        return dict(MeetingRequest.REGION_CHOICES)


class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = '__all__'

    def create(self, validated_data):
        return NewsletterSubscription.objects.create(**validated_data)

