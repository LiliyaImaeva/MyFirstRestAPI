# Generated by Django 2.1.1 on 2018-09-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20180913_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='roles',
            field=models.ManyToManyField(to='api.Roles'),
        ),
    ]
