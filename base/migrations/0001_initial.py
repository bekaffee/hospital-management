# Generated by Django 4.0.4 on 2022-11-04 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('iin_number', models.IntegerField()),
                ('id_number', models.IntegerField()),
                ('name_surname_middlename', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency_contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('martial_status', models.CharField(blank=True, max_length=100, null=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('other_details', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name_surname_middlename'],
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('iin_number', models.IntegerField()),
                ('id_number', models.IntegerField()),
                ('name_surname_middlename', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('department_id', models.CharField(blank=True, max_length=100, null=True)),
                ('specialization_details_id', models.CharField(blank=True, max_length=100, null=True)),
                ('experience_in_years', models.IntegerField()),
                ('photo_of_the_doctor', models.ImageField(upload_to=None)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('price_of_the_appointment', models.CharField(blank=True, max_length=100, null=True)),
                ('schedule_details', models.CharField(blank=True, max_length=100, null=True)),
                ('degree_or_education', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('homepage_url', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name_surname_middlename'],
            },
        ),
    ]
