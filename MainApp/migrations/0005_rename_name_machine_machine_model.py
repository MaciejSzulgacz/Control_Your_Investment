# Generated by Django 3.2.1 on 2021-05-08 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_alter_machine_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='name',
            new_name='machine_model',
        ),
    ]