# Generated by Django 2.1.7 on 2019-03-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_info', '0018_auto_20190302_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]