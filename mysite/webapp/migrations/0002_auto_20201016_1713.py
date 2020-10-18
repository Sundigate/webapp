# Generated by Django 3.1.2 on 2020-10-16 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationstable',
            name='authors',
        ),
        migrations.AddField(
            model_name='publicationstable',
            name='author_id',
            field=models.IntegerField(default=1, verbose_name='ID автора'),
            preserve_default=False,
        ),
    ]
