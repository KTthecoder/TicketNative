# Generated by Django 4.1.5 on 2023-01-23 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='homeApp.categoriesmodel'),
            preserve_default=False,
        ),
    ]
