# Generated by Django 4.0.4 on 2022-05-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0005_alter_sitebanner_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitebanner',
            name='position',
            field=models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزئیات محصولات'), ('article_detail', 'صفحه مقالات'), ('article_list', 'صفحه جزئیات مقالات'), ('about_us', 'صفحه تماس با ما'), ('all_pages', '+++تمامی صفحات+++')], max_length=200, verbose_name='محل قرارگیری'),
        ),
    ]
