# Generated by Django 3.2.11 on 2022-01-21 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(default=0)),
                ('cow_milk', models.IntegerField(default=0)),
                ('goat_milk', models.IntegerField(default=0)),
                ('apple', models.IntegerField(default=0)),
                ('bananna', models.IntegerField(default=0)),
                ('egg', models.IntegerField(default=0)),
                ('apple_juice', models.IntegerField(default=0)),
                ('rice', models.IntegerField(default=0)),
                ('teether', models.IntegerField(default=0)),
                ('rice_cookie', models.IntegerField(default=0)),
                ('puff', models.IntegerField(default=0)),
                ('morning_good', models.IntegerField(default=0)),
                ('night_good', models.IntegerField(default=0)),
                ('chicken', models.IntegerField(default=0)),
                ('beef', models.IntegerField(default=0)),
                ('pork', models.IntegerField(default=0)),
                ('pears', models.IntegerField(default=0)),
                ('avocado', models.IntegerField(default=0)),
                ('evening_good', models.IntegerField(default=0)),
                ('dry_seaweed', models.IntegerField(default=0)),
                ('baby_broccoli', models.IntegerField(default=0)),
                ('egg_york', models.IntegerField(default=0)),
                ('asparagus', models.IntegerField(default=0)),
                ('carrot', models.IntegerField(default=0)),
                ('red_bean', models.IntegerField(default=0)),
                ('seaweed', models.IntegerField(default=0)),
                ('tomato', models.IntegerField(default=0)),
                ('spinach', models.IntegerField(default=0)),
                ('yam', models.IntegerField(default=0)),
                ('sea_bass', models.IntegerField(default=0)),
            ],
        ),
    ]
