# Generated by Django 3.1.7 on 2021-03-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20210307_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default="{% static 'community/logo.jpeg' %}", upload_to='community/image/%Y/%M/%D'),
        ),
    ]
