# Generated by Django 4.0.1 on 2022-01-28 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='conetent',
            new_name='content',
        ),
    ]