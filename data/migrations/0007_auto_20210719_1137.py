# Generated by Django 3.1.2 on 2021-07-19 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_siswa_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siswa',
            old_name='user',
            new_name='username',
        ),
    ]
