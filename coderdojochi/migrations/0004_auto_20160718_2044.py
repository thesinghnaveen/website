# Generated by Django 1.9.6 on 2016-07-18 20:44


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0003_auto_20160712_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='location',
        ),
        migrations.AddField(
            model_name='equipment',
            name='force_update_on_next_boot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equipment',
            name='last_system_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='last_system_update_check_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='uuid',
            field=models.CharField(default=b'000-000-000-000', max_length=255, verbose_name=b'UUID'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='aquisition_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
