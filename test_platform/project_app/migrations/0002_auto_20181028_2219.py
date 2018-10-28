# Generated by Django 2.1.1 on 2018-10-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='status',
        ),
        migrations.AlterField(
            model_name='module',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(default='', max_length=100, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='projectmanage',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='projectmanage',
            name='description',
            field=models.TextField(default='', max_length=100, verbose_name='描述'),
        ),
    ]
