# Generated by Django 5.1 on 2024-08-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuser',
            name='age',
            field=models.IntegerField(default=-1),
        ),
    ]
