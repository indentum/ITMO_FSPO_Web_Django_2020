# Generated by Django 3.1.3 on 2020-11-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navalpolice', '0002_auto_20201104_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]