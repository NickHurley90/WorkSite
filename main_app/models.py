from django.db import models


# Create your models here.

class Employer(models.Model):
    business_email = models.EmailField(unique=True)
    business_address = models.CharField(max_length=255)
    business_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username
    
class StaffRegister(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    trade_category = models.CharField(max_length=100)
    experience = models.TextField()
    staff_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username
    
class JobListing(models.Model):
    title = models.CharField(max_length=255)
    listing_id = models.CharField(max_length=20, unique=True)
    business_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.TextField()
    trade_category = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

class JobRegistration(models.Model):
    listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffRegister, on_delete=models.CASCADE)
    authorized_to_work = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.staff} registered for {self.listing.title}'