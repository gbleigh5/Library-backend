# Generated by Django 3.0.4 on 2020-03-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=120)),
                ('year_of_release', models.IntegerField()),
                ('category', models.TextField()),
            ],
        ),
    ]
