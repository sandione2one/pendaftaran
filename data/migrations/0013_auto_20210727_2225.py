# Generated by Django 3.1.2 on 2021-07-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_siswa_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='profile_pic',
            field=models.ImageField(blank=True, default='fotokosong.gif', upload_to=''),
        ),
    ]
