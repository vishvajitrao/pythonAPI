# Generated by Django 2.2.5 on 2019-09-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(help_text='Please enter email', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(help_text='Please enter First Name', max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(help_text='Please enter Last Name', max_length=20),
        ),
    ]
