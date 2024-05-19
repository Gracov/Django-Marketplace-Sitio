# Generated by Django 4.2.6 on 2024-05-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediasCommodities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.CharField(max_length=100)),
                ('media_ult_ano', models.FloatField()),
                ('media_ult_sem', models.FloatField()),
                ('media_ult_tri', models.FloatField()),
                ('media_ult_mes', models.FloatField()),
                ('variacao_ano', models.FloatField()),
                ('variacai_sem', models.FloatField()),
                ('variacao_tri', models.FloatField()),
                ('variacao_mes', models.FloatField()),
                ('data', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Media Movel de Commodities',
                'verbose_name_plural': 'Medias Moveis de Commodities',
                'ordering': ['ativo', 'data'],
            },
        ),
    ]
