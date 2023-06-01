# Generated by Django 3.2.18 on 2023-05-31 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('captions', models.TextField(blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=250)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('captions', models.TextField(blank=True, max_length=250)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=250)),
                ('images', models.ManyToManyField(to='gallery.Photo')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
