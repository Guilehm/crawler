# Generated by Django 2.1.5 on 2019-02-04 22:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='core/datafile/file')),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
