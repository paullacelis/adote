# Generated by Django 3.2.19 on 2023-06-29 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('divulgar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('estado', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('P', 'Para adoção'), ('A', 'Adotado')], default='P', max_length=1)),
                ('raca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='divulgar.raca')),
                ('tags', models.ManyToManyField(to='divulgar.Tag')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
