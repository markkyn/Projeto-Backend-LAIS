# Generated by Django 4.0.3 on 2022-03-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_group_grupo_pai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='grupo_pai',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
