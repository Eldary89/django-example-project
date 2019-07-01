# Generated by Django 2.2.2 on 2019-06-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=254)),
                ('tel_number', models.IntegerField()),
                ('avatar', models.ImageField(upload_to='')),
                ('registered_time', models.DateTimeField()),
            ],
        ),
    ]