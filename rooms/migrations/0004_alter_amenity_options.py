# Generated by Django 4.1.3 on 2022-11-25 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_room_name_alter_amenity_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
    ]
