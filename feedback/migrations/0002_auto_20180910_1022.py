# Generated by Django 2.1.1 on 2018-09-10 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='creted',
            new_name='created',
        ),
    ]
