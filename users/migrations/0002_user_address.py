# Generated by Django 3.0.7 on 2020-10-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
