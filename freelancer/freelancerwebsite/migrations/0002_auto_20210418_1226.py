# Generated by Django 3.2 on 2021-04-18 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelancerwebsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='language',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='reviewee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other', to='freelancerwebsite.freelance'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='freelancerwebsite.freelance'),
        ),
    ]
