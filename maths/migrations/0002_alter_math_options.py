# Generated by Django 4.0.6 on 2022-07-31 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='math',
            options={'ordering': ['-id']},
        ),
    ]
