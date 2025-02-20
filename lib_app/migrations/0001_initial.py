# Generated by Django 5.1.5 on 2025-01-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('publication_date', models.DateField(verbose_name='15-01-2004')),
                ('is_available', models.BooleanField(default=True)),
                ('edition', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
