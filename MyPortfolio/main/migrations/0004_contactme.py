# Generated by Django 4.1.5 on 2023-02-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_blog_image_replay'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cf_name', models.CharField(max_length=512)),
                ('cf_email', models.CharField(max_length=512)),
                ('cf_message', models.TextField()),
            ],
        ),
    ]
