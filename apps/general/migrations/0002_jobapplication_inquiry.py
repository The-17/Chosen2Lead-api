# Generated by Django 5.1.7 on 2025-03-16 12:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('referral', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('level_of_education', models.CharField(max_length=200)),
                ('course_of_study', models.CharField(blank=True, max_length=500, null=True)),
                ('house_address', models.TextField()),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=10)),
                ('cover_letter', models.TextField()),
                ('references', models.TextField()),
                ('terms_agreement', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.service')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
