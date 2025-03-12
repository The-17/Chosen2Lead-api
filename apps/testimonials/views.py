from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Testimonial
from .serializers import TestimonialListSerializer, CreateTestimonialSerialzier
from rest_framework.pagination import PageNumberPagination


class TestimonialListCreateAPIView(APIView, PageNumberPagination):
    serializer_class = TestimonialListSerializer
    post_serializer = CreateTestimonialSerialzier
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        testimonials = Testimonial.objects.all()

        self.page_size = 10
        paginated_queryset = self.paginate_queryset(testimonials, request, view=self)
        serializer = self.serializer_class(paginated_queryset, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.post_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Testimonial uploaded successfully",
            "data":serializer.data
            }, status=status.HTTP_201_CREATED)
    
