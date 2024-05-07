# Generated by Django 4.2.2 on 2024-04-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_alter_chessgame_whiteplayer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chessgame',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'PENDING'), ('a', 'ACTIVE'), ('f', 'FINISHED')], default='PENDING', help_text='Disponibilidad del libro', max_length=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(default='', help_text='The name of the Player', max_length=100, unique=True),
        ),
    ]
