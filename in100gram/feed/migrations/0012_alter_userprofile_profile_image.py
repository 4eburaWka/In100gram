# Generated by Django 4.2.2 on 2023-07-13 12:42

from django.db import migrations, models
import feed.models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0011_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='/profile_photos/logo.jpg', upload_to=feed.models.get_user_profile_photo_path),
        ),
    ]
