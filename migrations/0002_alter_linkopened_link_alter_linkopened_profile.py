# Generated by Django 4.2.1 on 2023-10-11 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_remove_profile_work_of_interest'),
        ('link_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkopened',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link_manager.link'),
        ),
        migrations.AlterField(
            model_name='linkopened',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
