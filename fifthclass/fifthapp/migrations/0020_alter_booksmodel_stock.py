# Generated by Django 5.1.4 on 2025-02-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifthapp', '0019_alter_ordermodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='stock',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
