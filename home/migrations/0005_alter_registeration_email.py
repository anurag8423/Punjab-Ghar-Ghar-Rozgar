# Generated by Django 5.0 on 2023-12-15 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_registeration_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
