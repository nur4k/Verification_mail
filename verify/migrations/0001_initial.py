# Generated by Django 4.1.5 on 2023-01-10 15:41

from django.db import migrations, models
import verify.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='phone number')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('is_verified', models.BooleanField(default=False, verbose_name='verified')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'unique_together': {('username', 'email', 'phone')},
            },
            managers=[
                ('objects', verify.managers.UserManager()),
            ],
        ),
    ]
