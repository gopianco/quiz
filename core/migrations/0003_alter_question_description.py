# Generated by Django 4.1 on 2022-08-27 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_question_options_question_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=600, verbose_name='Descrição'),
        ),
    ]
