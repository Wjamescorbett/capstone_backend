# Generated by Django 3.2.8 on 2022-01-15 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quoteShare', '0005_userfavorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='postedcomment',
            name='postedQuote',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quoteShare.postedquote'),
            preserve_default=False,
        ),
    ]
