# Generated by Django 3.1.4 on 2021-06-26 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaMPRO', '0016_merge_20210626_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario_bodega',
            field=models.BooleanField(default=False, null=True, verbose_name='Bodeguero'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario_contador',
            field=models.BooleanField(default=False, null=True, verbose_name='Contador'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario_vend',
            field=models.BooleanField(default=False, null=True, verbose_name='Vendedor'),
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta_id', models.FloatField(default=0.0)),
                ('monto', models.FloatField(default=1.0)),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('mensaje', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TiendaMPRO.ordendecompra')),
            ],
        ),
    ]
