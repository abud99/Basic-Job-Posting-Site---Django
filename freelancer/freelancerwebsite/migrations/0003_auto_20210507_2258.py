# Generated by Django 3.2 on 2021-05-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancerwebsite', '0002_auto_20210418_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='jobID',
        ),
        migrations.AddField(
            model_name='category',
            name='jobID',
            field=models.ManyToManyField(to='freelancerwebsite.job'),
        ),
    ]
