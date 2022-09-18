from django.db import models
import uuid

# Create your models here.
class Company(models.Model):
    UUID = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100)
    CEO = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    Inception_date = models.DateField()

class Team(models.Model):
    UUID = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    CompanyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    Lead_Name = models.CharField(max_length=100)
