from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    iin_number = models.IntegerField(null=True, blank=True)
    id_number = models.IntegerField(null=True, blank=True)
    name_surname_middlename = models.CharField(max_length=100, null=True, blank=True)
    blood_group = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    martial_status = models.CharField(max_length=100, null=True, blank=True)
    registration_date = models.DateTimeField(null=True, blank=True)
    other_details = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name_surname_middlename

    class Meta:
        ordering = ['name_surname_middlename']


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    iin_number = models.IntegerField(null=True, blank=True)
    id_number = models.IntegerField(null=True, blank=True)
    name_surname_middlename = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    department_id = models.CharField(max_length=100, null=True, blank=True)
    specialization_details_id = models.CharField(max_length=100, null=True, blank=True)
    experience_in_years = models.IntegerField(null=True, blank=True)
    photo_of_the_doctor = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True, blank=True)
    category =models.CharField(max_length=100, null=True, blank=True)
    price_of_the_appointment = models.CharField(max_length=100, null=True, blank=True)
    schedule_details = models.CharField(max_length=100, null=True, blank=True)
    degree_or_education = models.CharField(max_length=100, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    homepage_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_surname_middlename

    class Meta:
        ordering = ['name_surname_middlename']


class Admingo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']