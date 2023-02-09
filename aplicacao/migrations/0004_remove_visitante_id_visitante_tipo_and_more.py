# Generated by Django 4.0.2 on 2022-02-18 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0003_visitante_delete_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitante',
            name='id',
        ),
        migrations.AddField(
            model_name='visitante',
            name='tipo',
            field=models.CharField(choices=[('VS', 'Visitante'), ('MR', 'Morador')], default='VS', max_length=2),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='placa',
            field=models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='Placa'),
        ),
    ]
