# Generated by Django 4.1.6 on 2023-02-22 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_app', '0022_alter_brand_section_add_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.CharField(blank=True, max_length=80)),
                ('instagram_link', models.CharField(blank=True, max_length=80)),
                ('twitter_link', models.CharField(blank=True, max_length=80)),
                ('google_plus_link', models.CharField(blank=True, max_length=80)),
                ('company_name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Social_media',
                'verbose_name_plural': 'Social_medias',
            },
        ),
        migrations.DeleteModel(
            name='Our_clicnt',
        ),
    ]
