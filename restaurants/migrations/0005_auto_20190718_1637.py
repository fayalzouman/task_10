# Generated by Django 2.1.5 on 2019-07-18 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20190718_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant'),
        ),
    ]