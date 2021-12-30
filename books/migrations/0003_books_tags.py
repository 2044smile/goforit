# Generated by Django 4.0 on 2021-12-30 09:50

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('books', '0002_alter_books_total_page_alter_pages_read_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
