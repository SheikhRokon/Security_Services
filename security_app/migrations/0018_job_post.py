# Generated by Django 4.1.6 on 2023-02-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_app', '0017_remove_video_gallery_videofile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jop_type', models.CharField(max_length=40)),
                ('job_position', models.CharField(max_length=40)),
                ('vacancy', models.CharField(max_length=40)),
                ('last_date_of_application', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Job_Post',
                'verbose_name_plural': 'Job_Posts',
            },
        ),
    ]
