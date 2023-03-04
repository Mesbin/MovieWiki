# Generated by Django 3.2.16 on 2023-03-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('f_id', models.AutoField(db_column='F_id', primary_key=True, serialize=False)),
                ('movie_name', models.CharField(db_column='Movie_name', max_length=50)),
                ('year', models.IntegerField(db_column='Year')),
                ('discription', models.CharField(db_column='Discription', max_length=100)),
                ('date', models.DateField(db_column='Date')),
                ('rating', models.CharField(db_column='Rating', max_length=10)),
                ('reply', models.CharField(db_column='Reply', max_length=50)),
            ],
            options={
                'db_table': 'feedback',
                'managed': False,
            },
        ),
    ]