# Generated by Django 3.2.9 on 2021-11-25 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='image', upload_to='articles/'),
        ),
    ]
