# Generated by Django 4.0.3 on 2022-04-14 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tshirt', '0002_alter_tshirt_photo_alter_tshirt_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='photo',
            field=models.ImageField(null=True, upload_to='tshirt/static/img/tshirts/'),
        ),
    ]
