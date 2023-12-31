# Generated by Django 4.2.2 on 2023-06-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='followers_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='followings_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='posts_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
