# Generated by Django 5.1.4 on 2024-12-10 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoría de Produecto', 'verbose_name_plural': 'Categorías de Productos'},
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]