# Generated by Django 3.1.2 on 2021-07-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20210726_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
