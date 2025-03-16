from django.db import models
import uuid

class BaseModel(models.Model):
    """Base model for all other models."""
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    linkedin = models.URLField(blank=True, null=True)
    ig = models.URLField(blank=True, null=True, help_text="Instagram")
    x = models.URLField(blank=True, null=True)
    fb = models.URLField(blank=True, null=True, help_text="Facebook")
    contact_email = models.EmailField(null=True, blank=True)
    support_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class Service(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.title


class faq(BaseModel):
    question = models.CharField(max_length=500, help_text="The question being asked")
    answer = models.CharField(max_length=500, help_text="The answer to the question")

    def __str__(self):
        return self.question


class Inquiry(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)


class JobApplication(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    referral = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    level_of_education = models.CharField(max_length=200)
    course_of_study = models.CharField(max_length=500, null=True, blank=True)
    house_address = models.TextField()
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=10)
    cover_letter = models.TextField()
    references = models.TextField()
    terms_agreement = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name}, {self.position}"

