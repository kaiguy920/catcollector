# Generated by Django 3.0 on 2022-04-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_cattoy'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='cattoys',
            field=models.ManyToManyField(to='main_app.CatToy'),
        ),
    ]
