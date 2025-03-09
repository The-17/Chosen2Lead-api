from django.urls import path
from .views import ServicesListAPIView, CompanyDetailAPIView, FAQAPIView

urlpatterns = [
    path("services/", ServicesListAPIView.as_view(), name="services"),
    path("company-detail/", CompanyDetailAPIView.as_view(), name="company-info"),
    path("faqs/", FAQAPIView.as_view(), name="faqs")
]
