# Generated by Django 5.1 on 2024-09-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="joined_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="member",
            name="phone",
            field=models.IntegerField(null=True),
        ),
    ]
