from django.db import models
from apps.general.models import BaseModel
from cloudinary.models import CloudinaryField
from .validators import video_file_validator

class Testimonial(BaseModel):
    full_name = models.CharField(max_length=300)
    company = models.CharField(max_length=300, null=True, blank=True)
    position_in_company = models.CharField(max_length=300, null=True, blank=True)
    video = CloudinaryField("video", resource_type="video", folder="Testimonials",
                            validators=[video_file_validator])
    rating = models.SmallIntegerField(default=5)

    def __str__(self):
        return f"{self.full_name} - {self.rating} Stars"
    
