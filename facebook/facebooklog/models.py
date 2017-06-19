from django.db import models

class facebook(models.Model):
	name=models.CharField(max_length=255)
	lastname=models.CharField(max_length=255)
	email=models.CharField(max_length=50)
	paswd=models.CharField(max_length=50)
	day=models.CharField(max_length=50)
	month=models.CharField(max_length=50)
	year=models.CharField(max_length=50)
	gen=models.CharField(max_length=50)