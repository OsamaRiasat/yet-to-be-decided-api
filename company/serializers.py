from rest_framework import serializers
from .models import ContactSubmission



class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'

    def create(self, validated_data):
        return ContactSubmission.objects.create(**validated_data)

    def get_region_choices(self):
        return dict(ContactSubmission.REGION_CHOICES)
