# Generated by Django 4.0.4 on 2022-07-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0007_productgallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='product_files/'),
        ),
    ]
