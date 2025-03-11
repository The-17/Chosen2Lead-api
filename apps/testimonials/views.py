from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Testimonial
from .serializers import TestimonialListSerializer
from rest_framework.pagination import PageNumberPagination


class TestimonialListCreateAPIView(APIView, PageNumberPagination):
    serializer_class = TestimonialListSerializer

    def get(self, request):
        testimonials = Testimonial.objects.all()

        self.page_size = 10
        paginated_queryset = self.paginate_queryset(testimonials, request, view=self)
        serializer = self.serializer_class(paginated_queryset, many=True)

        return self.get_paginated_response(serializer.data)

    
