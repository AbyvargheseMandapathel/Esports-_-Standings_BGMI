# Generated by Django 4.2.6 on 2023-10-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('matches', models.IntegerField()),
                ('win', models.IntegerField()),
                ('fp', models.IntegerField()),
                ('pp', models.IntegerField()),
                ('tp', models.IntegerField()),
            ],
        ),
    ]
