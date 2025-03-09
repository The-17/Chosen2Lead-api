from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Service, Company, faq
from .serializers import ServicesSerializer, CompanySerializer, FaqSerializer


class ServicesListAPIView(APIView):
    serializer_class = ServicesSerializer

    def get(self, request):
        services = Service.objects.all()
        serializer = self.serializer_class(services, many=True)

        return Response({
            "message": "services retrieved successfully",
            "data":serializer.data
            }, status=status.HTTP_200_OK)


class CompanyDetailAPIView(APIView):
    serializer_class = CompanySerializer

    def get(self, request):
        company = Company.objects.filter().first()
        serializer = self.serializer_class(company)

        return Response({
            "message": "company info retrieved successfully",
            "data":serializer.data
            }, status=status.HTTP_200_OK)


class FAQAPIView(APIView):
    serializer_class = FaqSerializer

    def get(self, request):
        faqs = faq.objects.all()
        serializer = self.serializer_class(faqs, many=True)

        return Response({
            "message": "FAQs retrieved successfully",
            "data":serializer.data
            }, status=status.HTTP_200_OK)

