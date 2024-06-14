# Generated by Django 5.0.6 on 2024-06-14 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('foto', models.ImageField(upload_to='servicios/')),
                ('descripcion', models.TextField()),
            ],
        ),
    ]