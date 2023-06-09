# Generated by Django 4.1.5 on 2023-05-06 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('picture', models.URLField(default='https://openlibrary.org/images/icons/avatar_author-lg.png', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('ISBN', models.CharField(max_length=13)),
                ('synopsis', models.TextField(blank=True)),
                ('cover', models.URLField(null=True)),
                ('authors', models.ManyToManyField(to='bookapp.author')),
                ('genres', models.ManyToManyField(to='bookapp.genre')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.language')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.publisher')),
            ],
        ),
    ]
