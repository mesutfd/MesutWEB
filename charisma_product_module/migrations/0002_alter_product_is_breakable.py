# Generated by Django 3.2.14 on 2022-07-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charisma_product_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_breakable',
            field=models.CharField(choices=[('breakable', 'شکستنی'), ('un_beakable', 'غیر شکستنی')], max_length=255, verbose_name='آیا شکستنیست؟'),
        ),
    ]
