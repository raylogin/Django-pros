# Generated by Django 3.2.3 on 2021-06-13 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odoc', '0002_alter_docplace_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docplace',
            name='Last_used',
        ),
    ]
