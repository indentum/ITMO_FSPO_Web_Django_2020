# Generated by Django 3.1.1 on 2020-09-29 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('auto_id', models.IntegerField(primary_key=True, serialize=False)),
                ('color', models.CharField(choices=[('Black', 'Black'), ('Yellow', 'Yellow'), ('White', 'White'), ('Green', 'Green'), ('Blue', 'Blue')], max_length=10)),
                ('license_plate', models.CharField(max_length=6)),
                ('model', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('owner_id', models.IntegerField(primary_key=True, serialize=False)),
                ('birthday', models.DateField()),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Possession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rec', models.DateField()),
                ('date_end', models.DateField()),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstLab.auto')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstLab.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id_cert', models.IntegerField(primary_key=True, serialize=False)),
                ('release_date', models.DateField()),
                ('type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('M', 'M')], max_length=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstLab.owner')),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='own',
            field=models.ManyToManyField(through='FirstLab.Possession', to='FirstLab.Owner'),
        ),
    ]
