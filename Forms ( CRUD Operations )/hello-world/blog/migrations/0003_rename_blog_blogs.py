# Generated by Django 3.2.11 on 2022-02-02 12:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20220202_1753'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blog',
            new_name='Blogs',
        ),
    ]
