# Generated by Django 4.1.3 on 2023-02-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('passoword', models.CharField(max_length=32)),
            ],
        ),
    ]
