from django.db import models

class MyData(models.Model):
    emp_num = models.CharField(max_length=255)
    emp_name = models.CharField(max_length=255)