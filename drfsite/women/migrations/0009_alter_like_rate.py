# Generated by Django 4.1.3 on 2022-11-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0008_women_author_1_alter_women_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='rate',
            field=models.PositiveIntegerField(choices=[(1, 'Ok'), (2, 'Good'), (3, 'Fine'), (4, 'Amazing'), (5, 'Incredible')], null=True),
        ),
    ]