# Generated by Django 3.1.1 on 2020-09-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0003_companylinks_mainframecontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companylinks',
            options={'verbose_name': 'links', 'verbose_name_plural': 'Company links'},
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='phone_number_2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
