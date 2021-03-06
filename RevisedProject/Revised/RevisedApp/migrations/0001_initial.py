# Generated by Django 3.0 on 2021-05-23 07:41

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cord_name', models.CharField(max_length=10, null=True)),
                ('dept', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('CIVIL', 'CIVIL'), ('Mechanical', 'Mechanical'), ('EEE', 'EEE'), ('MBA', 'MBA')], max_length=12, null=True)),
                ('phone_no', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jobinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=20)),
                ('salary', models.IntegerField(null=True)),
                ('skills', models.CharField(max_length=30)),
                ('job_role', models.CharField(max_length=30)),
                ('eligible_percent', models.IntegerField(null=True)),
                ('eligible_dept', models.CharField(max_length=30)),
                ('year_of_pass', models.IntegerField(null=True)),
                ('last_date', models.DateField(null=True)),
                ('descrip', models.CharField(max_length=250)),
                ('com_image', models.ImageField(default='123.jpg', upload_to='Jobs/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rollno', models.CharField(default='17AK1A000', max_length=10)),
                ('dob', models.DateField(null=True)),
                ('year', models.CharField(choices=[('III', 'III'), ('IV', 'IV')], max_length=5, null=True)),
                ('dept', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('CIVIL', 'CIVIL'), ('Mechanical', 'Mechanical'), ('EEE', 'EEE'), ('MBA', 'MBA')], max_length=12, null=True)),
                ('phone_no', models.IntegerField(null=True)),
                ('percentage', models.IntegerField(null=True)),
                ('backlogs', models.IntegerField(null=True)),
                ('pass_year', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('role', models.IntegerField(choices=[(1, 'coordinator'), (2, 'Student'), (3, 'Guest')], default=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
