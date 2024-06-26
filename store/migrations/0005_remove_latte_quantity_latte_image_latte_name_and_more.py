# Generated by Django 4.1 on 2024-04-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_latte_image_remove_latte_name_latte_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latte',
            name='quantity',
        ),
        migrations.AddField(
            model_name='latte',
            name='image',
            field=models.ImageField(default=1, upload_to='latte_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='latte',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='latte',
            name='flavor',
            field=models.CharField(choices=[('caramel', 'Caramel'), ('vanilla', 'Vanilla'), ('hazelnut', 'Hazelnut'), ('cinnamon', 'Cinnamon')], max_length=20),
        ),
        migrations.AlterField(
            model_name='latte',
            name='size',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=20),
        ),
    ]
