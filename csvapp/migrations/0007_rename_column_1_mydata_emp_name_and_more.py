# Generated by Django 4.1.7 on 2023-03-21 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvapp', '0006_rename_employee_mydata_column_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mydata',
            old_name='column_1',
            new_name='emp_name',
        ),
        migrations.RenameField(
            model_name='mydata',
            old_name='column_2',
            new_name='emp_num',
        ),
    ]
