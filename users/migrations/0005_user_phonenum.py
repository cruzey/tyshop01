# Generated by Django 3.0.7 on 2020-10-28 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_cart_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phonenum',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
