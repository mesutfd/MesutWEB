# Generated by Django 4.0.4 on 2022-05-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='url_title',
            field=models.CharField(db_index=True, default='url_title', max_length=700, verbose_name='نام برند در url'),
            preserve_default=False,
        ),
    ]
