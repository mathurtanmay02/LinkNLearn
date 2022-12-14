# Generated by Django 4.1.3 on 2022-11-05 17:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('courseid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('course_name', models.CharField(default='', max_length=200)),
                ('course_detail', models.CharField(default='', max_length=200)),
                ('cover_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
