# Generated by Django 4.1.6 on 2023-02-18 12:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_app', '0012_rename_news_news_add_page_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSR_add_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csr_date', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='CSRImage')),
                ('csr_details', ckeditor.fields.RichTextField(default='aaa')),
            ],
            options={
                'verbose_name': 'CSR_add_page',
                'verbose_name_plural': 'CSR_add_pages',
            },
        ),
    ]
