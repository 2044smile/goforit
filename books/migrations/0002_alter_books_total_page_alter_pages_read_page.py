# Generated by Django 4.0 on 2021-12-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='total_page',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pages',
            name='read_page',
            field=models.IntegerField(null=True),
        ),
    ]
