# Generated by Django 3.2.14 on 2022-07-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charisma_product_module', '0002_alter_product_is_breakable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='file',
        ),
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.IntegerField(blank=True, null=True, verbose_name='مالیات'),
        ),
    ]
