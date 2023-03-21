# Generated by Django 4.1.7 on 2023-03-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvapp', '0002_mydata_delete_csvdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mydata',
            old_name='column_1',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='mydata',
            name='column_2',
        ),
        migrations.AlterField(
            model_name='mydata',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
