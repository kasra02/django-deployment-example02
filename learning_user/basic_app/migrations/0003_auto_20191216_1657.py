# Generated by Django 2.2.5 on 2019-12-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_user2'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('content', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='user2',
        ),
    ]
