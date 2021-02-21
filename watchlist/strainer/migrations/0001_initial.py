# Generated by Django 3.1.6 on 2021-02-10 12:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(db_index=True, max_length=254)),
                ('watchlist', models.JSONField(null=True)),
                ('radar', models.JSONField(null=True)),
            ],
        ),
    ]