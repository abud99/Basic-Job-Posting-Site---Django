# Generated by Django 3.2 on 2021-04-15 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='freelance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancerwebsite.freelance')),
            ],
        ),
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished_on', models.DateField()),
                ('jobID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancerwebsite.job')),
                ('workerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancerwebsite.freelance')),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancerwebsite.freelance')),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('jobID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancerwebsite.job')),
            ],
        ),
    ]