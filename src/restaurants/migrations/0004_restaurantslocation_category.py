# Generated by Django 2.0.2 on 2018-07-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20180726_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantslocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]