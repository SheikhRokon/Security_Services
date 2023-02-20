# Generated by Django 4.1.6 on 2023-02-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_app', '0007_about_descriptions_banner_descriptions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management_term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Management_termImage')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('profile_details', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Management_term',
                'verbose_name_plural': 'Management_terms',
            },
        ),
    ]
