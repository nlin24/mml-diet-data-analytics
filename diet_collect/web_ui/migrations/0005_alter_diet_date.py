# Generated by Django 3.2.11 on 2022-01-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ui', '0004_auto_20220121_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
