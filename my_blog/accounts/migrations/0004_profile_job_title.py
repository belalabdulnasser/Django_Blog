# Generated by Django 2.1.5 on 2019-02-24 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job_title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
