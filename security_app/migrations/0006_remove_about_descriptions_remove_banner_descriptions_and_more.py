# Generated by Django 4.1.6 on 2023-02-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_app', '0005_board_of_directors_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='descriptions',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='descriptions',
        ),
        migrations.RemoveField(
            model_name='board_of_directors',
            name='first_part',
        ),
        migrations.RemoveField(
            model_name='board_of_directors',
            name='secend_part',
        ),
        migrations.AlterField(
            model_name='board_of_directors',
            name='image',
            field=models.ImageField(upload_to='BoardOfDirectors'),
        ),
        migrations.AlterField(
            model_name='board_of_directors',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]