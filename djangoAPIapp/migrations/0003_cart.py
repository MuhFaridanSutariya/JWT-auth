# Generated by Django 4.0.4 on 2022-05-23 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('djangoAPIapp', '0002_alter_category_options_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('books', models.ManyToManyField(to='djangoAPIapp.book')),
                ('products', models.ManyToManyField(to='djangoAPIapp.product')),
            ],
            options={
                'ordering': ['cart_id', '-created_at'],
            },
        ),
    ]