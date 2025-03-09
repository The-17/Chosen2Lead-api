from rest_framework import serializers
from .models import Service, faq, Company


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


