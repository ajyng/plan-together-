# Generated by Django 3.1.7 on 2021-03-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='website_url',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
