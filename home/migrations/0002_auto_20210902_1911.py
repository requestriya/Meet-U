# Generated by Django 3.0.7 on 2021-09-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='Age',
            field=models.DateField(),
        ),
    ]
