# Generated by Django 3.2 on 2022-01-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_img',
            field=models.ImageField(blank=True, default='default-blog.jpg', null=True, upload_to=''),
        ),
    ]
