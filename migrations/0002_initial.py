# Generated by Django 4.2 on 2024-02-20 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('link_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkopened',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
