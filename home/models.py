# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Estimate(models.Model):

    #__Estimate_FIELDS__
    product_name = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    final_trim_size_height = models.IntegerField(null=True, blank=True)
    final_trim_size_width = models.IntegerField(null=True, blank=True)
    binding_type = models.CharField(max_length=255, null=True, blank=True)
    inks_used = models.TextField(max_length=255, null=True, blank=True)
    auxiliary_operations = models.TextField(max_length=255, null=True, blank=True)
    estimated_cost = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Estimate_FIELDS__END

    class Meta:
        verbose_name        = _("Estimate")
        verbose_name_plural = _("Estimate")



#__MODELS__END
