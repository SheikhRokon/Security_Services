# Generated by Django 4.1.6 on 2023-02-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_app', '0024_alter_social_media_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_media',
            name='company_name',
            field=models.CharField(max_length=80),
        ),
    ]
