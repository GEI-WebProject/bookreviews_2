# Generated by Django 4.1.5 on 2023-04-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='sinopsys',
            field=models.CharField(max_length=2000),
        ),
    ]