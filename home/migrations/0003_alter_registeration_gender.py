# Generated by Django 5.0 on 2023-12-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_registeration_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='gender',
            field=models.CharField(default='Male', max_length=12),
        ),
    ]
