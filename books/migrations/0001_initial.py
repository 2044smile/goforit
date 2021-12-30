# Generated by Django 4.0 on 2021-12-30 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(help_text='Books', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('total_page', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(help_text='Pages', primary_key=True, serialize=False)),
                ('read_page', models.IntegerField()),
                ('save_time', models.DateTimeField(auto_now=True)),
                ('books_id', models.ForeignKey(db_column='books_id', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.books')),
            ],
        ),
    ]
