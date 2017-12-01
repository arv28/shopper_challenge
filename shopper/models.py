# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', 
        message="Phone number must be entered in the format: '+19999999999'. Should be 10 digit number.")

class Shopper(models.Model):
    """
    Model for shopper
    """
    id = models.AutoField(serialize=False, primary_key=True)
    name = models.CharField(max_length=50)
    
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    application_date = models.DateField(db_index=True, default=timezone.now)
    workflow_state = models.CharField(max_length=100, default='applied')
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return '{},{},{},{},{}'.format(self.id, self.name, self.phone, self.email, self.state)
