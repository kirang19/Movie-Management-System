# Generated by Django 3.1.7 on 2024-06-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_remove_booking_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='m_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]