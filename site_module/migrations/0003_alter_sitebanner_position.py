# Generated by Django 4.0.4 on 2022-05-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_sitebanner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitebanner',
            name='position',
            field=models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزئیات محصولات'), ('about_us', 'صفحه تماس با ما')], max_length=200, verbose_name='محل قرارگیری'),
        ),
    ]
