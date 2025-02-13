# Generated by Django 5.1.5 on 2025-02-13 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tv_show', '0003_alter_filmmodel_music_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('choice_status', models.CharField(choices=[('Просмотрел', 'Просмотрел'), ('Не просмотрел', 'Не просмотрел')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('choice_film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tv_show.filmmodel')),
            ],
        ),
    ]
