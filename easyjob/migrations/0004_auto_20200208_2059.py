# Generated by Django 2.2.7 on 2020-02-08 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyjob', '0003_auto_20200204_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='cCompanyName',
            new_name='CompanyName',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='cEmail',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='cLocation',
            new_name='Location',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='cMobile',
            new_name='Mobile',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='cVacancyNumber',
            new_name='VacancyNumber',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='cVacantPost',
            new_name='VacantPost',
        ),
    ]