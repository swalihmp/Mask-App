# Generated by Django 3.2.3 on 2022-10-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maskapp', '0006_rename_user_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
