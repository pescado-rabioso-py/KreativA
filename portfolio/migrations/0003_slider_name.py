# Generated by Django 3.2.4 on 2021-06-21 23:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
