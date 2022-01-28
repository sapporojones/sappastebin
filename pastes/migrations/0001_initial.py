# Generated by Django 4.0.1 on 2022-01-27 22:48

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pastes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('paste_body', models.TextField()),
            ],
        ),
    ]