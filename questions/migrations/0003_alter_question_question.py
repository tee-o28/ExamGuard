# Generated by Django 4.1.2 on 2022-10-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]
