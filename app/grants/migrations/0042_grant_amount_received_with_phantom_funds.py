# Generated by Django 2.2.4 on 2020-03-11 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0041_auto_20200207_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='amount_received_with_phantom_funds',
            field=models.DecimalField(decimal_places=2, default=0, help_text='The fundingamount across all rounds with phantom funding', max_digits=20),
        ),
    ]