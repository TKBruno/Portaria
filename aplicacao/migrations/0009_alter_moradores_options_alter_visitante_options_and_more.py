# Generated by Django 4.0.2 on 2022-02-18 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0008_moradores_delete_morador_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moradores',
            options={'ordering': ['endereco', 'nome_completo']},
        ),
        migrations.AlterModelOptions(
            name='visitante',
            options={'ordering': ['nome_completo']},
        ),
        migrations.RenameField(
            model_name='moradores',
            old_name='nome_Completo',
            new_name='nome_completo',
        ),
        migrations.RenameField(
            model_name='visitante',
            old_name='nome_Completo',
            new_name='nome_completo',
        ),
        migrations.AlterModelTable(
            name='moradores',
            table='Moradores',
        ),
        migrations.AlterModelTable(
            name='visitante',
            table='Visitante',
        ),
    ]
