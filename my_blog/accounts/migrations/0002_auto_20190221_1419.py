# Generated by Django 2.1.5 on 2019-02-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='p_default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
