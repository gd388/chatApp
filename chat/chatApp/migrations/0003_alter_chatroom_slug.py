# Generated by Django 5.0 on 2024-01-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0002_alter_chatroom_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
