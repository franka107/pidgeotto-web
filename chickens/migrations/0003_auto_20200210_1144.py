# Generated by Django 3.0.2 on 2020-02-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chickens', '0002_promotion_week_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='week_age',
            field=models.IntegerField(default=1),
        ),
    ]
