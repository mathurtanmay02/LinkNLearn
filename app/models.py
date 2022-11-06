import uuid
from django.db import models

class resume(models.Model):
    name = models.CharField(max_length= 200, default='', unique=True)
    contact = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200, default='' , unique=True)
    about_me = models.CharField(max_length=200, default='')
    career_objective = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class course(models.Model):
    courseid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=200, default='' , null = False)
    course_detail = models.CharField(max_length=200, default='' , null = False)
    cover_image = models.ImageField(null = False, blank= False)

    def __str__(self):
        return self.course_name

