# Generated by Django 5.1.7 on 2025-03-11 20:31

import apps.testimonials.validators
import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_alter_testimonial_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='video',
            field=cloudinary.models.CloudinaryField(max_length=255, validators=[apps.testimonials.validators.video_file_validator], verbose_name='video'),
        ),
    ]
