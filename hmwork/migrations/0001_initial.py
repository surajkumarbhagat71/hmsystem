# Generated by Django 2.2.7 on 2020-05-13 01:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('hopital_img', models.ImageField(upload_to='media/')),
                ('owner_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=200)),
                ('addresh', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stap',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('degree', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/')),
                ('data_time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hmwork.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Pasent',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(default='optional', max_length=254)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gander', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=200)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hmwork.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('degree', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/')),
                ('data_time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hmwork.Hospital')),
            ],
        ),
    ]
