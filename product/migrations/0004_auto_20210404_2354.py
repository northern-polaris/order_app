# Generated by Django 3.1.6 on 2021-04-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210404_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code_year',
            field=models.IntegerField(null=True),
        ),
    ]