# Generated by Django 5.0 on 2023-12-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=255),
        ),
    ]
