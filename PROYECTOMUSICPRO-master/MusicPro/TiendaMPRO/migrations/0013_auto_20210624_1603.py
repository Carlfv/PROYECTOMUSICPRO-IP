# Generated by Django 3.2.3 on 2021-06-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaMPRO', '0012_remove_estrategiadeventa_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario_bodega',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario_contador',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario_vend',
            field=models.BooleanField(default=False),
        ),
    ]
