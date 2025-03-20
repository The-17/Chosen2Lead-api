from django.urls import path
from .views import (
    ServicesListAPIView, 
    CompanyDetailAPIView, 
    FAQAPIView,
    InquiryAPIView,
    JobApplicationAPIView
)

urlpatterns = [
    path("services/", ServicesListAPIView.as_view(), name="services"),
    path("company-detail/", CompanyDetailAPIView.as_view(), name="company-info"),
    # path("faqs/", FAQAPIView.as_view(), name="faqs"),
    # path("inquiry/", InquiryAPIView.as_view(), name="inquiry"),
    # path("job-application/", JobApplicationAPIView.as_view(), name="job-application")
]
