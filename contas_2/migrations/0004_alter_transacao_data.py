# Generated by Django 4.1 on 2022-08-23 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas_2', '0003_alter_transacao_data_alter_transacao_observações'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]