# Generated by Django 4.2.2 on 2023-06-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher', models.CharField(max_length=255)),
                ('studenets', models.CharField(max_length=255)),
                ('grade', models.IntegerField()),
            ],
        ),
    ]
