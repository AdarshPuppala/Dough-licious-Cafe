# Generated by Django 4.1 on 2024-04-20 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_espresso'),
    ]

    operations = [
        migrations.AddField(
            model_name='espresso',
            name='flavor',
            field=models.CharField(choices=[('Original', 'Original')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
