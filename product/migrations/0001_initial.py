# Generated by Django 3.0.4 on 2020-03-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('low_price', models.CharField(max_length=200)),
                ('n_review', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]
