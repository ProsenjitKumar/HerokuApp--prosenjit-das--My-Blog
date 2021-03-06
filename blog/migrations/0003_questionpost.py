# Generated by Django 2.1.4 on 2019-01-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190101_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('publish', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
