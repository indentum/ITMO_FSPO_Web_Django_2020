# Generated by Django 3.0.4 on 2020-04-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_auto_20200415_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cars',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.Auto'),
        ),
    ]
