# Generated by Django 2.0 on 2018-02-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_auto_20180216_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='user_ip',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
