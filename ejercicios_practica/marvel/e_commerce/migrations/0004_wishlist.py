# Generated by Django 3.2.2 on 2023-10-28 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_commerce', '0003_delete_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('favorite', models.BooleanField(default=False, verbose_name='favorite')),
                ('cart', models.BooleanField(default=False, verbose_name='cart')),
                ('wished_qty', models.PositiveBigIntegerField(default=0, verbose_name='wished_qty')),
                ('bought_qty', models.PositiveBigIntegerField(default=0, verbose_name='bought_qty')),
                ('comic', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.comic', verbose_name='Comic')),
                ('user', models.ForeignKey(blank=True, default='new user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'wishlist',
                'verbose_name_plural': 'wishlists',
                'db_table': 'e_commerce_wishlist',
            },
        ),
    ]
