# Generated by Django 3.1.7 on 2021-03-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='logo.jpeg', upload_to='community/image/%Y/%M/%D'),
        ),
    ]