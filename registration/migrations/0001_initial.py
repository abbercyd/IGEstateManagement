# Generated by Django 4.0.4 on 2022-04-20 13:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='no-avatar.png', upload_to=registration.models.get_avatar_path)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_tenant', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserNotifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.userdata')),
            ],
            options={
                'verbose_name': 'Notifications',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Tenants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=10)),
                ('id_front', models.ImageField(blank=True, upload_to=registration.models.get_user_docs_path)),
                ('id_back', models.ImageField(blank=True, upload_to=registration.models.get_user_docs_path)),
                ('active_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('policy_agreement', models.BooleanField(default=False)),
                ('moved_in', models.BooleanField(default=False)),
                ('move_in_date', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('associated_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.userdata', verbose_name='tenant')),
            ],
            options={
                'verbose_name_plural': 'Tenants',
            },
        ),
        migrations.CreateModel(
            name='RelatedRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=155, null=True)),
                ('file', models.FileField(upload_to=registration.models.get_related_record_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.tenants')),
            ],
            options={
                'verbose_name': 'Related Records',
                'verbose_name_plural': 'Related Records',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('street_address', models.CharField(max_length=30)),
                ('lga_area', models.CharField(max_length=30)),
                ('state', models.CharField(default='Kenya', max_length=30)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.userdata')),
            ],
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=100, null=True)),
                ('id_back', models.ImageField(help_text='Must be a valid ID!', upload_to=registration.models.get_user_docs_path)),
                ('id_front', models.ImageField(help_text='Must be a valid ID!', upload_to=registration.models.get_user_docs_path)),
                ('active_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('whatsapp_number', models.CharField(max_length=14)),
                ('status', models.CharField(choices=[('rv', 'Revoked'), ('pv', 'Pending Approval'), ('ap', 'Approved')], default='pv', max_length=3)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='added_by', to='registration.userdata')),
                ('associated_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.userdata')),
            ],
            options={
                'verbose_name_plural': 'Managers',
            },
        ),
    ]
