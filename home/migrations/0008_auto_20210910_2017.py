# Generated by Django 3.0.7 on 2021-09-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210910_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_images',
            name='images2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
