# Generated by Django 4.0.4 on 2022-05-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoAPIapp', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='John Doe', max_length=100),
        ),
    ]
