# Generated by Django 4.0.4 on 2022-07-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stripe_payment_module', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.TextField(max_length=255, verbose_name='مشخصات خرید')),
            ],
        ),
    ]
