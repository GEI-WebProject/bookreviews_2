# Generated by Django 4.1.5 on 2023-04-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_alter_book_sinopsys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='sinopsys',
            field=models.TextField(blank=True),
        ),
    ]
