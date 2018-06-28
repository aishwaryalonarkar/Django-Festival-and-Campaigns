# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class festmodel(models.Model):
	date = models.IntegerField(default=1)
	month = models.CharField(max_length=200)
	year = models.IntegerField(default=2018)
	religion = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	festival_name = models.CharField(max_length=200)
	description = models.CharField(max_length=9000)
	offers = models.CharField(max_length=200)
	event_type = models.CharField(max_length=200,default=None)

	def __str__(self):
  		return self.festival_name


@python_2_unicode_compatible
class campaign(models.Model):
	festival = models.ForeignKey(festmodel,on_delete=models.CASCADE,default=None)
	campaign_name = models.CharField(max_length=500,default=None)
	start_date = models.DateField(default=1)
	end_date = models.DateField(default=1)
	co_ordinator = models.CharField(max_length=500)
	campaign_type = models.CharField(max_length=500)
	email_content = models.TextField()
	sms_content = models.TextField()
	email_subject = models.TextField()
	target_count = models.IntegerField(default=0)
	leads_generated = models.IntegerField()

	def __str__(self):
  		return self.campaign_name

