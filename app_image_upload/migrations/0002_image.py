# Generated by Django 5.0.6 on 2024-06-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_image_upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
