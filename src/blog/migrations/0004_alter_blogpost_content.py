# Generated by Django 4.1.7 on 2023-03-25 13:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
