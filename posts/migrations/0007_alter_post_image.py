# Generated by Django 4.0.6 on 2022-08-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
