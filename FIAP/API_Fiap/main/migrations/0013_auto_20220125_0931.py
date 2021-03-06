# Generated by Django 3.2.9 on 2022-01-25 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20220125_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiap',
            name='dataFinal',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 9, 31, 52, 879922), null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 9, 31, 52, 879922)),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 9, 31, 52, 881915)),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataFinal',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 25, 9, 31, 52, 877932), null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dataInicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 25, 9, 31, 52, 877932), null=True),
        ),
    ]
