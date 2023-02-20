# Generated by Django 4.1.6 on 2023-02-18 08:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_app', '0009_our_clicnt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clicnts_testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Clicnts_testimonialsImage')),
                ('company_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Clicnts_testimonials',
                'verbose_name_plural': 'Clicnts_testimonialss',
            },
        ),
        migrations.CreateModel(
            name='Contract_signing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Clicnts_testimonialsImage')),
                ('company_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Clicnts_testimonials',
                'verbose_name_plural': 'Clicnts_testimonialss',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_part', ckeditor.fields.RichTextField(default='aaa')),
                ('image', models.ImageField(upload_to='HistoryImage')),
                ('secend_part', ckeditor.fields.RichTextField(default='aaa')),
                ('company_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Clicnts_testimonials',
                'verbose_name_plural': 'Clicnts_testimonialss',
            },
        ),
    ]
