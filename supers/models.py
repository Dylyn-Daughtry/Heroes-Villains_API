from django.db import models

from super_types.models import SuperTypes

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=255, null=True)
    alter_ego = models.CharField(max_length=255, null=True)
    primary_ability = models.CharField(max_length=255, null=True)
    secondary_ability = models.CharField(max_length=255, null=True)
    catchphrase = models.CharField(max_length=255, null=True)
    super_type = models.ForeignKey(SuperTypes, on_delete=models.CASCADE)