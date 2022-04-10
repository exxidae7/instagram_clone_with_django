# Generated by Django 4.0.3 on 2022-04-09 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True)),
                ('bio', models.TextField(max_length=500)),
                ('gender', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=200)),
                ('count_post', models.IntegerField(default=0)),
                ('follow', models.IntegerField(default=0)),
                ('followers', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.SlugField(max_length=255)),
                ('image', models.ImageField(upload_to='upload/')),
                ('dataPost', models.DateTimeField()),
                ('caption', models.TextField(max_length=1000)),
                ('like', models.IntegerField()),
                ('comment', models.TextField(max_length=2000)),
                ('namePost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]
