# Generated by Django 3.2.8 on 2022-01-06 09:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quoteShare', '0003_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='PostedComment',
        ),
    ]