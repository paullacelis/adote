# Generated by Django 3.2.19 on 2023-07-05 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='fotos_pet')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('estado', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=14)),
                ('status', models.CharField(choices=[('p', 'Para adocao'), ('A', 'Adotado')], max_length=1)),
                ('raca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='divulgar.raca')),
                ('tag', models.ManyToManyField(to='divulgar.Tag')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
