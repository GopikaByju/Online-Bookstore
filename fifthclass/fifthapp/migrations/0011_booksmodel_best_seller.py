# Generated by Django 5.1.4 on 2025-02-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifthapp', '0010_booksmodel_category_alter_booksmodel_book_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='best_seller',
            field=models.BooleanField(default=False),
        ),
    ]
