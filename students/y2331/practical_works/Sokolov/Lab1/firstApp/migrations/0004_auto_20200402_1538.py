# Generated by Django 3.0.5 on 2020-04-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_auto_20200402_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]