# Generated by Django 3.0.4 on 2020-04-29 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='id',
        ),
        migrations.AddField(
            model_name='banner',
            name='page_to_display',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='member',
            name='roll_number',
            field=models.CharField(default='191CS299', max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='member',
            name='sig',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='post',
            field=models.CharField(max_length=300),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='mysite.Member')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]