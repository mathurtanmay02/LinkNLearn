# Generated by Django 4.1.3 on 2022-11-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='authorization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50, unique=True)),
                ('name', models.CharField(default='', max_length=200, unique=True)),
                ('position', models.CharField(default='', max_length=50)),
                ('company_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='connect',
        ),
    ]