# Generated by Django 2.1 on 2019-09-14 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sith_recruiting', '0002_auto_20190914_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='is_shadow_hand',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recruitsresult',
            name='recruit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sith_recruiting.Recruit'),
            preserve_default=False,
        ),
    ]