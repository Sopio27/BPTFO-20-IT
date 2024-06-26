# Generated by Django 5.0.6 on 2024-06-15 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_department_imagesource'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='TeamDescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='DepartmentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.department'),
        ),
    ]
