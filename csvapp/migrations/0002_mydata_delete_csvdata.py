# Generated by Django 4.1.7 on 2023-03-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_1', models.CharField(max_length=255)),
                ('column_2', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='CSVData',
        ),
    ]
