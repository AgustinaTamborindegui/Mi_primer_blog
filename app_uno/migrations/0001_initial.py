# Generated by Django 4.0.1 on 2022-06-30 04:21

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('contenido', models.CharField(max_length=2000)),
                ('fecha', models.DateField()),
                ('nombre_libro', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('lanzamiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=500)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('creado_en', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creado_en', to='app_uno.post')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creado_por', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
