# Generated by Django 3.1.3 on 2020-11-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StuffTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
