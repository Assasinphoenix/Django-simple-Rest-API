# Generated by Django 2.1.7 on 2019-06-23 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('emp_id', models.IntegerField(unique=True)),
                ('salary', models.IntegerField()),
                ('department', models.CharField(max_length=20)),
            ],
        ),
    ]
