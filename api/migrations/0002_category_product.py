# Generated by Django 3.1.3 on 2020-11-24 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_tag', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
