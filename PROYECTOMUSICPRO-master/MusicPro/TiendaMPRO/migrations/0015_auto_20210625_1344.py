# Generated by Django 3.1.4 on 2021-06-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaMPRO', '0014_auto_20210625_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordendecompra',
            name='pagado',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='transferencia',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
