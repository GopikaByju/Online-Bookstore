# Generated by Django 5.1.4 on 2025-02-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifthapp', '0007_alter_offersmodel_offer_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True)),
                ('edition', models.CharField(blank=True, max_length=100, null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, default='English', max_length=100, null=True)),
                ('cover_type', models.CharField(choices=[('Hardcover', 'Hardcover'), ('Paperback', 'Paperback'), ('eBook', 'eBook')], max_length=50)),
                ('rating', models.FloatField(blank=True, default=0.0, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('stock_status', models.BooleanField(blank=True, default=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('book_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('paper_quality', models.CharField(blank=True, max_length=100, null=True)),
                ('print_type', models.CharField(choices=[('Black & White', 'Black & White'), ('Color', 'Color')], default='Black & White', max_length=100)),
                ('binding', models.CharField(choices=[('Perfect Bound', 'Perfect Bound'), ('Spiral Bound', 'Spiral Bound')], default='Perfect Bound', max_length=100)),
            ],
        ),
    ]
