# Generated by Django 5.0.6 on 2024-06-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_department_imagesource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='ImageSource',
            field=models.CharField(blank=True, null=True),
        ),
    ]
