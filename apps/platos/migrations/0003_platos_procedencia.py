# Generated by Django 4.2.1 on 2023-06-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0002_alter_platos_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='platos',
            name='procedencia',
            field=models.CharField(default='', max_length=75),
        ),
    ]
