# Generated by Django 4.1.3 on 2023-05-28 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_annotation_annotation_body_annotation_annotation_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='annotation',
        ),
    ]
