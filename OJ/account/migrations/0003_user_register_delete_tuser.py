# Generated by Django 5.1 on 2024-08-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_tuser_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='tuser',
        ),
    ]
