# Generated by Django 3.0.7 on 2021-09-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210911_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='dp',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]