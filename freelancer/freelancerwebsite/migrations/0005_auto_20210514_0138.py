# Generated by Django 3.2 on 2021-05-13 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancerwebsite', '0004_alter_job_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='status',
        ),
        migrations.AddField(
            model_name='job',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
