# Generated by Django 5.0.6 on 2024-06-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_employeerole_table_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='ImageSource',
            field=models.CharField(default='https://img.pikbest.com/ai/illus_our/20230427/4ba0131d1c5c3f8c5cce8657cfaba3cf.jpg!w700wp'),
            preserve_default=False,
        ),
    ]
