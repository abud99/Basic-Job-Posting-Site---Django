# Generated by Django 3.2 on 2021-05-13 22:38

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('freelancerwebsite', '0007_job_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='job',
            name='categories',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Programming'), ('item_key2', 'Graphic Design'), ('item_key3', 'General'), ('item_key4', 'Hardware'), ('item_key5', 'Django')], default='Hello', max_length=49),
        ),
    ]
