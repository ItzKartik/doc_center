# Generated by Django 3.1.1 on 2020-09-18 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='types',
            fields=[
                ('type_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='docs',
            fields=[
                ('doc_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('doc_name', models.CharField(max_length=200)),
                ('doc', models.FileField(upload_to='docs/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amt', models.IntegerField()),
                ('bid_date', models.DateTimeField(auto_now=True)),
                ('linker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc_center_app.docs')),
            ],
        ),
    ]
