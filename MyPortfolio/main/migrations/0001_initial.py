# Generated by Django 4.1.6 on 2023-02-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
            ],
        ),
    ]
