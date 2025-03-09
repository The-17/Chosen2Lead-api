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

