# Generated by Django 3.1.6 on 2021-02-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ManyToManyField(to='product.ProductCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='default_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterModelTable(
            name='product',
            table='itw_product',
        ),
        migrations.AlterModelTable(
            name='productcategory',
            table='itw_product_category',
        ),
        migrations.DeleteModel(
            name='ProductProductCategory',
        ),
    ]
