from rest_framework import serializers
from .models import ContactSubmission, MeetingRequest, NewsletterSubscription



class ContactSubmissionSerializer(serializers.ModelSerializer):
    opt_in = serializers.BooleanField(required=False)
    class Meta:
        model = ContactSubmission
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        if validated_data.get('opt_in') is True:
            # Create a newsletter subscription
            NewsletterSubscription.objects.create(email=validated_data.get('email'))
            print('Newsletter subscription created')
        # remove the opt_in field from the validated data
        validated_data.pop('opt_in', None)
        return ContactSubmission.objects.create(**validated_data)


class MeetingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRequest
        fields = '__all__'

    def create(self, validated_data):
        return MeetingRequest.objects.create(**validated_data)



class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = '__all__'

    def create(self, validated_data):
        return NewsletterSubscription.objects.create(**validated_data)

