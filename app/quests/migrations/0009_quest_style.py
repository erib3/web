# Generated by Django 2.2.3 on 2019-10-14 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0008_questpointaward'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='style',
            field=models.CharField(choices=[('Quiz', 'quiz'), ('Example for Demo', 'example_demo')], default='quiz', max_length=100),
        ),
    ]
