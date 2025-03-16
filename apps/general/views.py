from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Service, 
    Company, 
    faq, 
    Inquiry
)
from .serializers import (
    ServicesSerializer, 
    CompanySerializer, 
    FaqSerializer, 
    InquirySerializer,
    JobApplicationSerializer
)
from drf_spectacular.utils import extend_schema

class ServicesListAPIView(APIView):
    serializer_class = ServicesSerializer

    @extend_schema(
            summary="Get services",
            description="""
                This endpoint retreives all the services rendered by Chosen2Lead
                """
    )
    def get(self, request):
        services = Service.objects.all()
        serializer = self.serializer_class(services, many=True)

        return Response({
            "message": "services retrieved successfully",
            "data":serializer.data
            }, status=status.HTTP_200_OK)


class CompanyDetailAPIView(APIView):
    serializer_class = CompanySerializer

    @extend_schema(
            summary="Get Chosen2Lead Info",
            description="""
                This endpoint retreives all information about CHosen2Lead
                """
    )
    def get(self, request):
        company = Company.objects.filter().first()
        serializer = self.serializer_class(company)

        return Response({
            "message": "company info retrieved successfully",
            "data":serializer.data
            }, status=status.HTTP_200_OK)


class FAQAPIView(APIView):
    serializer_class = FaqSerializer

    @extend_schema(
            summary="Get FAQs",
            description="""
                This endpoint retreives all Frequently Asked Questions and their answer
                """
    )
    def get(self, request):
        faqs = faq.objects.all()
        serializer = self.serializer_class(faqs, many=True)

        return Response({
            "message": "FAQs retrieved successfully",
            "data":serializer.data
            }, status=status.HTTP_200_OK)


class InquiryAPIView(APIView):
    serializer_class = InquirySerializer

    @extend_schema(
            summary="Submit service inquiries",
            description="""
                This endpoint creates a new service inquiry and sends an email to chosen2lead
                """
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "inquiry Submitted successfully",
            "data":serializer.data
            }, status=status.HTTP_201_CREATED)
    

class JobApplicationAPIView(APIView):
    serializer_class = JobApplicationSerializer

    @extend_schema(
            summary="Submit Job application",
            description="""
                This endpoint creates a new sejob application and sends an email to chosen2lead
                """
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Application Submitted successfully",
            "data":serializer.data
            }, status=status.HTTP_201_CREATED)