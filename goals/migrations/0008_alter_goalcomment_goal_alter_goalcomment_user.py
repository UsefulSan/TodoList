# Generated by Django 4.1.6 on 2023-03-17 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0007_alter_goalcategory_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalcomment',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goals.goal', verbose_name='Цель'),
        ),
        migrations.AlterField(
            model_name='goalcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]