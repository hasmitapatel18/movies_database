# Generated by Django 2.1.7 on 2019-03-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_info', '0015_auto_20190302_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
