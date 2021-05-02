# Generated by Django 3.1.6 on 2021-04-04 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210202_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.IntegerField(default=1, verbose_name='kodi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='code_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
