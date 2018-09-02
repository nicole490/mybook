# Generated by Django 2.0.1 on 2018-08-13 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='作者名'),
        ),
    ]
