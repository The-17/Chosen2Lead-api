from rest_framework import serializers
from .models import Service, faq, Company, Inquiry, JobApplication


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ["created_at", "updated_at"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = faq
        fields = "__all__"


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry 
        fields = "__all__"


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"