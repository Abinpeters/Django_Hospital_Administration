# Generated by Django 4.2.5 on 2023-09-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0000000', max_length=50)),
                ('specialized', models.CharField(default='aaaa', max_length=100)),
                ('address', models.CharField(default='0000000', max_length=100)),
                ('number', models.IntegerField(default='0000000', max_length=50)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=255)),
                ('username', models.CharField(default='0000000', max_length=50)),
                ('password', models.IntegerField(default='000000', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0000000', max_length=50)),
                ('disease', models.CharField(default='aaa', max_length=100)),
                ('address', models.CharField(default='0000000', max_length=100)),
                ('number', models.CharField(default='0000000', max_length=50)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
