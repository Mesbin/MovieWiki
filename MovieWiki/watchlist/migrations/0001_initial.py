# Generated by Django 3.2.16 on 2023-03-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('w_id', models.AutoField(db_column='W_id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'watchlist',
                'managed': False,
            },
        ),
    ]
