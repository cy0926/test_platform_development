# Generated by Django 2.1.1 on 2018-10-15 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('description', models.CharField(default='', max_length=100, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('description', models.CharField(default='', max_length=100, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.ProjectManage'),
        ),
    ]
