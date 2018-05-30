from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from uuid import uuid4

class Listing(models.Model):
	# Borrowed from SO: https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	"""Django generated fields"""
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	"""Fields from Yelp API Call"""
	yelpID = models.CharField(max_length=100)
	yelpUrl = models.URLField('URL', unique=True)
	name = models.CharField(max_length=200)
	rating = models.IntegerField(max_length=1)
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	location = models.CharField(max_length=300)
