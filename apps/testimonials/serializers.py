from rest_framework import serializers
from .models import Testimonial
from .validators import ALLOWED_TYPES

class TestimonialListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class CreateTestimonialSerialzier(serializers.ModelSerializer):
    video = serializers.FileField()
    class Meta:
        model = Testimonial
        exclude = ["id", "created_at", "updated_at"]

    def validate(self, attrs):
        video = attrs.get("video")
        if not video:
            raise serializers.ValidationError("Video is required.")
        
        return super().validate(attrs)

    def validate_video(self, video):
        """ Validate the uploaded video file type """
        
        if video.content_type not in ALLOWED_TYPES:
            raise serializers.ValidationError("Invalid file type. Only mp4 videos are allowed.")
        return video