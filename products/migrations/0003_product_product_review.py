# Generated by Django 4.0.3 on 2022-04-01 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_rename_review_number_review_number_rating'),
        ('products', '0002_product_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_review',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='reviews.review'),
            preserve_default=False,
        ),
    ]