from rest_framework import serializers
from .models import Testimonial

class TestimonialListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"