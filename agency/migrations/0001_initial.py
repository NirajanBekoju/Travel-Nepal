# Generated by Django 3.1 on 2020-08-26 07:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('registered_date', models.DateTimeField(blank=True, verbose_name=datetime.datetime.now)),
                ('agent_id', models.ForeignKey(limit_choices_to={'is_agency': True}, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
