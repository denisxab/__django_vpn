# Generated by Django 3.2.8 on 2021-10-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openvpn',
            name='user_name_get',
            field=models.TextField(db_column='Имя получателя'),
        ),
    ]
